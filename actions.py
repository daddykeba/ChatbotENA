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
from dbConnect import getData

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


class AdmissibiliteForm(FormAction):

    def name(self) -> Text:
        return "admissibilite_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["num", "prenom", "nom"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "num": [self.from_entity(entity="num"), self.from_text(not_intent=["deny","stop","affirm"])],
            "prenom": [self.from_entity(entity="prenom"), self.from_text(not_intent=["deny", "stop","affirm"])],
            "nom": [self.from_entity(entity="nom"), self.from_text(not_intent=["deny", "stop","affirm"])],
        }


    def validate_num(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ) -> Dict[Text, Any]:

        query = "select * from flask.admissions where id= "+ value + ";"

        data = getData(query)

        if (len(data)>0):
            return {"num": value}
        else:
            dispatcher.utter_message(text="Votre numéro est invalide")
            return {"num": None}


    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ## type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        num = tracker.get_slot("num")
        prenom = tracker.get_slot("prenom")
        nom = tracker.get_slot("nom")

        query = "select * from flask.admissions where id="+ num + ";"

        data = getData(query)
        for row in data:
            centre = row[9]
            salle = row[10]
            table = row[11]
            date = row[8]
            if(len(centre)>0):
                response = "{} {}, la date des épreuves d'admissibilité est {}".format(prenom,nom,date)
                response1 = "votre centre est {} à la salle {} avec comme numéro de table {}".format(centre,salle,table)
                dispatcher.utter_message(response)
                dispatcher.utter_message(response1)
            else:
                response = "{} {} les informations que vous avez saisi sont incorrectes ".format(prenom, nom)
                dispatcher.utter_message(response)
                dispatcher.utter_message(text="Réssayer à nouveau en reprenant votre question")

        return [ SlotSet("num",None),SlotSet("prenom",None),SlotSet("nom",None)]