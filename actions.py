# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import requests
import time
import re
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted, SlotSet, SessionStarted, ActionExecuted, EventType

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_iamabot")
        dispatcher.utter_message(template="utter_greet")

        return [UserUtteranceReverted()]

class MyFallbackAction(Action):

    def name(self) -> Text:
        return "my_fallback_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_ask_rephrase")

        return []

class ActionConcours(Action):

    def name(self) -> Text:
        return "action_concours"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        concoursAll = tracker.get_slot("concoursAll")

        if (concoursAll == 'direct a' or concoursAll == "cycle a"):
            dispatcher.utter_message(template="utter_concoursDA")
            return [SlotSet("concoursAll","direct a")]
        if (concoursAll == 'direct b' or concoursAll == "cycle b"):
            dispatcher.utter_message(template="utter_concoursDB")
            return [SlotSet("concoursAll", "direct b")]
        if (concoursAll == 'professionnel a'):
            dispatcher.utter_message(template="utter_concoursPA")
            return [SlotSet("concoursAll","professionnel a")]
        if (concoursAll == 'professionnel b'):
            dispatcher.utter_message(template="utter_concoursPB")
            return [SlotSet("concoursAll", "professionnel b")]

class ActionInscriptionEna(Action):

    def name(self) -> Text:
        return "action_inscription_ena"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        list_da = ['direct a', 'cycle a']
        list_db = ['direct b', 'cycle b']
        prof_a = ['professionnel a', 'professionnelle a']
        prof_b = ['professionnel b', 'professionnelle b']


        inscrire = tracker.get_slot("inscrire")
        concoursAll = tracker.get_slot("concoursAll")

        if (inscrire != 'None' and concoursAll in list_da):
            dispatcher.utter_message(template="uttter_inscriptionDA")
            return []
        if (inscrire != 'None' and concoursAll in list_db):
            dispatcher.utter_message(template="uttter_inscriptionDB")
            return []
        if (inscrire != 'None' and concoursAll in prof_a):
            dispatcher.utter_message(template="uttter_inscriptionPA")
            return []
        if (inscrire != 'None' and concoursAll in prof_b):
            dispatcher.utter_message(template="uttter_inscriptionPB")
            return []


class ActionPay(Action):

    def name(self) -> Text:
        return "action_pay"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        list_path = ['ena', 'concours']
        list_da = ['direct a', 'cycle a']
        list_db = ['direct b', 'cycle b']
        prof_a = ['professionnel a', 'professionnelle a']
        prof_b = ['professionnel b', 'professionnelle b']

        concoursAll = tracker.get_slot("concoursAll")
        pay = tracker.get_slot("pay")

        if(concoursAll in list_da):
            dispatcher.utter_message(template="utter_payDA")
            return []
        if (concoursAll in list_db):
            dispatcher.utter_message(template="utter_payDB")
            return []
        if (concoursAll in prof_a):
            dispatcher.utter_message(template="utter_payPA")
            return []
        if (concoursAll in prof_b):
            dispatcher.utter_message(template="utter_payPB")
            return []


class ActionRequire(Action):

    def name(self) -> Text:
        return "action_require"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        list_da = ['direct a', 'cycle a']
        list_db = ['direct b', 'cycle b']
        prof_a = ['professionnel a', 'professionnelle a']
        prof_b = ['professionnel b', 'professionnelle b']

        concoursAll = tracker.get_slot("concoursAll")
        requirement = tracker.get_slot("requirement")

        if(concoursAll in list_da):
            dispatcher.utter_message(template="utter_requireDA")
            return []
        if (concoursAll in list_db):
            dispatcher.utter_message(template="utter_requireDB")
            return []
        if (concoursAll in prof_a):
            dispatcher.utter_message(template="utter_requirePA")
            return []
        if (concoursAll in prof_b):
            dispatcher.utter_message(template="utter_requirePB")
            return []
