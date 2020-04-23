## default story
* out_of_scope
  - action_hello_world

## happy path
* greet
  - utter_greet
  
## happy path1
* greet
  - utter_greet
* get_info
  - utter_concours


## say goodbye
* goodbye
  - utter_goodbye
  
## get_info
* get_info
  - utter_concours
## get_info1
* get_info{"concoursAll": "direct a"}
  - action_concours
## get_info2
* get_info{"concoursAll": "direct b"}
  - action_concours
## get_info3
* get_info{"concoursAll": "professionnel a"}
  - action_concours
## get_info4
* get_info{"concoursAll": "professionnel b"}
  - action_concours
  
## concours_inscription
* concours_inscriptioon{"inscrire":"inscrire"}
  - utter_incrire_ena
  
## concours_inscription1
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
  
## concours_inscription2
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct b"}
  - action_inscription_ena
  
## concours_inscription3
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel a"}
  - action_inscription_ena

## concours_inscription4
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel b"}
  - action_inscription_ena
## concours_inscription5
* concours_inscriptioon{"inscrire":"inscrire", "open":"créer"}
  - action_inscription_ena
  
## pay  
* pay_concours{"pay":"frais"}
  - utter_pay_ena

## pay1
* pay_concours{"pay":"frais", "concoursAll":"direct a"}
  - action_pay
  
## pay5
* pay_concours{"pay":"frais", "concoursAll":"direct a"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay12
* greet
  - utter_greet
* pay_concours{"pay":"frais", "concoursAll":"direct a"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay2  
* pay_concours{"pay":"frais", "concoursAll":"direct b"}
  - action_pay
  
## pay6  
* pay_concours{"pay":"frais", "concoursAll":"direct b"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay11
* greet
  - utter_greet  
* pay_concours{"pay":"frais", "concoursAll":"direct b"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay3  
* pay_concours{"pay":"frais", "concoursAll":"professionnel a"}
  - action_pay
  
## pay7  
* pay_concours{"pay":"frais", "concoursAll":"professionnel a"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay10
* greet
  - utter_greet  
* pay_concours{"pay":"frais", "concoursAll":"professionnel a"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay4 
* pay_concours{"pay":"frais", "concoursAll":"professionnel b"}
  - action_pay
  
## pay8 
* pay_concours{"pay":"frais", "concoursAll":"professionnel b"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay9
* greet
  - utter_greet 
* pay_concours{"pay":"frais", "concoursAll":"professionnel b"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena

## require-1  
* requirement_concours{"requirement":"conditions"}
  - utter_require_ena
  
## require1
* requirement_concours{"requirement":"conditions", "concoursAll":"direct a"}
  - action_require
  
## require5
* requirement_concours{"requirement":"conditions", "concoursAll":"direct a"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay12
* greet
  - utter_greet
* requirement_concours{"requirement":"conditions", "concoursAll":"direct a"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require2  
* requirement_concours{"requirement":"conditions", "concoursAll":"direct b"}
  - action_require
  
## require6  
* requirement_concours{"requirement":"conditions", "concoursAll":"direct b"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require11
* greet
  - utter_greet  
* requirement_concours{"requirement":"conditions", "concoursAll":"direct b"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require3  
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel a"}
  - action_require
  
## require7  
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel a"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require10
* greet
  - utter_greet  
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel a"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require4 
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel b"}
  - action_require
  
## require8 
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel b"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require9
* greet
  - utter_greet 
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel b"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## mdp
* mdp{"modifie":"modifier", "password":"mot de passe"}
  - utter_mdp_ena
  
## mdp1
* greet
  - utter_greet
* mdp{"modifie":"modifier", "password":"mot de passe"}
  - utter_mdp_ena
  
## mdp2
* profile{"modifie":"modifier"}
  - utter_menu_modifie
* profile{"modifie":"modifier", "password":"mot de passe"}
  - utter_mdp_ena
  
  
## profile
* profile{"modifie":"modifier", "profils":"profil"}
  - utter_profile_ena
  
## profile2
* profile{"modifie":"modifier", "attributeProfile":"nom"}
  - utter_profile_ena
  
## profile8
* profile{"modifie":"modifier"}
  - utter_menu_modifie
* profile{"modifie":"modifier", "profils":"profil"}
  - utter_profile_ena
  
## connexion
* connexion{"inscrire":"compte", "connexions":"connecter"}
  - utter_connexion_ena
  
## connexion1
* connexion{"connexions":"connecter"}
  - utter_connexion_ena
  
## mailconfirm
* confirmMail{"inscrire":"inscription", "mail":"mail de confirmation"}
  - utter_mail_ena
  
## mailconfirm1
* confirmMail{"mail":"mail de confirmation"}
  - utter_mail_ena
  
## login
* greet
  - utter_greet 
* login{"logins":"login"}
  - utter_ask_login
  - utter_call_back
* goodbye
  - utter_goodbye
  
## login1
* greet
  - utter_greet 
* login{"logins":"login"}
  - utter_ask_login
  - utter_call_back
 
## login2
* login{"logins":"login"}
  - utter_ask_login
  - utter_call_back
* goodbye
  - utter_goodbye
  
## login3
* login{"logins":"login"}
  - utter_ask_login
  - utter_call_back
   
## login_connexion
* greet
  - utter_greet
* connexion{"connexions":"connecter"}
  - utter_connexion_ena
  - utter_call_back
* login{"logins":"login"}
  - utter_ask_login
  - utter_call_back
* goodbye
  - utter_goodbye 
  
## login_connexion1
* greet
  - utter_greet
* connexion{"connexions":"connecter"}
  - utter_connexion_ena
  - utter_call_back
* login{"logins":"login"}
  - utter_ask_login
  - utter_call_back

## login_connexion2
* connexion{"connexions":"connecter"}
  - utter_connexion_ena  
  - utter_call_back
* login{"logins":"login"}
  - utter_ask_login
  - utter_call_back
* goodbye
  - utter_goodbye
  
## login_connexion3
* connexion{"connexions":"connecter"}
  - utter_connexion_ena
  - utter_call_back   
* login{"logins":"login"}
  - utter_ask_login
  - utter_call_back

## help
* greet
  - utter_greet
* help
  - utter_concours
* goodbye
  - utter_goodbye
  
## help1
* greet
  - utter_greet
* help
  - utter_concours
  
## help2  
* help
  - utter_concours
* goodbye
  - utter_goodbye
  
## help3  
* help
  - utter_concours
  

  