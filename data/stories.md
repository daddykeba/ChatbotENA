## default story
* out_of_scope
  - action_hello_world
  
## chat     
* chat
   - respond_chat
   - utter_call_back

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
  
## concours_inscription6
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription7
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct b"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription8
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel a"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription9
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel b"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription10
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription11
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct b"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription12
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel a"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription13
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel b"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription14
* greet
  - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription15
* greet
  - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct b"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription16
* greet
  - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel a"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription17
* greet
  - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel b"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription18
* greet
  - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription19
* greet
  - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct b"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription20
* greet
  - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel a"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription21
* greet
  - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel b"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription22
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay

## concours_inscription23
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct b"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription24
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel a"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription25
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel b"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription26
* greet
 - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay

## concours_inscription27
* greet
 - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct b"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription28
* greet
 - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel a"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription29
* greet
 - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel b"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## concours_inscription30
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require

## concours_inscription31
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct b"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription32
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel a"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription33
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel b"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription34
* greet
 - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require

## concours_inscription35
* greet
 - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"direct b"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription36
* greet
 - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel a"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## concours_inscription37
* greet
 - utter_greet
* concours_inscriptioon{"inscrire":"inscrire", "concoursAll":"professionnel b"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay  
* pay_concours{"pay":"frais"}
  - utter_pay_ena

## pay1
* pay_concours{"pay":"frais", "concoursAll":"direct a"}
  - action_pay
  
## pay2
* pay_concours{"pay":"frais", "concoursAll":"direct a"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay3
* greet
  - utter_greet
* pay_concours{"pay":"frais", "concoursAll":"direct a"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay4  
* pay_concours{"pay":"frais", "concoursAll":"direct b"}
  - action_pay
  
## pay5  
* pay_concours{"pay":"frais", "concoursAll":"direct b"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay6
* greet
  - utter_greet  
* pay_concours{"pay":"frais", "concoursAll":"direct b"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay7  
* pay_concours{"pay":"frais", "concoursAll":"professionnel a"}
  - action_pay
  
## pay8  
* pay_concours{"pay":"frais", "concoursAll":"professionnel a"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay9
* greet
  - utter_greet  
* pay_concours{"pay":"frais", "concoursAll":"professionnel a"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay10 
* pay_concours{"pay":"frais", "concoursAll":"professionnel b"}
  - action_pay
  
## pay11 
* pay_concours{"pay":"frais", "concoursAll":"professionnel b"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay12
* greet
  - utter_greet 
* pay_concours{"pay":"frais", "concoursAll":"professionnel b"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay13
* pay_concours{"pay":"frais", "concoursAll":"direct a"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay14
* greet
  - utter_greet
* pay_concours{"pay":"frais", "concoursAll":"direct a"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay15  
* pay_concours{"pay":"frais", "concoursAll":"direct b"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay16
* greet
  - utter_greet  
* pay_concours{"pay":"frais", "concoursAll":"direct b"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay17  
* pay_concours{"pay":"frais", "concoursAll":"professionnel a"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay118
* greet
  - utter_greet  
* pay_concours{"pay":"frais", "concoursAll":"professionnel a"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay19 
* pay_concours{"pay":"frais", "concoursAll":"professionnel b"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay20
* greet
  - utter_greet 
* pay_concours{"pay":"frais", "concoursAll":"professionnel b"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay21
* pay_concours{"pay":"frais", "concoursAll":"direct a"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay22
* greet
  - utter_greet
* pay_concours{"pay":"frais", "concoursAll":"direct a"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay23
* pay_concours{"pay":"frais", "concoursAll":"direct a"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay24
* greet
  - utter_greet
* pay_concours{"pay":"frais", "concoursAll":"direct a"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay25  
* pay_concours{"pay":"frais", "concoursAll":"direct b"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay26
* greet
  - utter_greet  
* pay_concours{"pay":"frais", "concoursAll":"direct b"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay27  
* pay_concours{"pay":"frais", "concoursAll":"direct b"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay28
* greet
  - utter_greet  
* pay_concours{"pay":"frais", "concoursAll":"direct b"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay29  
* pay_concours{"pay":"frais", "concoursAll":"professionnel a"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay30
* greet
  - utter_greet  
* pay_concours{"pay":"frais", "concoursAll":"professionnel a"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay31  
* pay_concours{"pay":"frais", "concoursAll":"professionnel a"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay32
* greet
  - utter_greet  
* pay_concours{"pay":"frais", "concoursAll":"professionnel a"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay33 
* pay_concours{"pay":"frais", "concoursAll":"professionnel b"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay34
* greet
  - utter_greet 
* pay_concours{"pay":"frais", "concoursAll":"professionnel b"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* requirement_concours{"requirement":"conditions"}
  - action_require
  
## pay35 
* pay_concours{"pay":"frais", "concoursAll":"professionnel b"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay36
* greet
  - utter_greet 
* pay_concours{"pay":"frais", "concoursAll":"professionnel b"}
  - action_pay
* requirement_concours{"requirement":"conditions"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena

## require  
* requirement_concours{"requirement":"conditions"}
  - utter_require_ena
  
## require1
* requirement_concours{"requirement":"conditions", "concoursAll":"direct a"}
  - action_require
  
## require2
* requirement_concours{"requirement":"conditions", "concoursAll":"direct a"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require3
* greet
  - utter_greet
* requirement_concours{"requirement":"conditions", "concoursAll":"direct a"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require4  
* requirement_concours{"requirement":"conditions", "concoursAll":"direct b"}
  - action_require
  
## require5  
* requirement_concours{"requirement":"conditions", "concoursAll":"direct b"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require6
* greet
  - utter_greet  
* requirement_concours{"requirement":"conditions", "concoursAll":"direct b"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require7  
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel a"}
  - action_require
  
## require8  
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel a"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require9
* greet
  - utter_greet  
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel a"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require10 
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel b"}
  - action_require
  
## require11 
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel b"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require12
* greet
  - utter_greet 
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel b"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require13
* requirement_concours{"requirement":"conditions", "concoursAll":"direct a"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## require14
* greet
  - utter_greet
* requirement_concours{"requirement":"conditions", "concoursAll":"direct a"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## require15  
* requirement_concours{"requirement":"conditions", "concoursAll":"direct b"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## require16
* greet
  - utter_greet  
* requirement_concours{"requirement":"conditions", "concoursAll":"direct b"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## require17  
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel a"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## require18
* greet
  - utter_greet  
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel a"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## require19 
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel b"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## require20
* greet
  - utter_greet 
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel b"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
  
## require21
* requirement_concours{"requirement":"conditions", "concoursAll":"direct a"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## require22
* greet
  - utter_greet
* requirement_concours{"requirement":"conditions", "concoursAll":"direct a"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## require23
* requirement_concours{"requirement":"conditions", "concoursAll":"direct a"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require24
* greet
  - utter_greet
* requirement_concours{"requirement":"conditions", "concoursAll":"direct a"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require25  
* requirement_concours{"requirement":"conditions", "concoursAll":"direct b"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## require26
* greet
  - utter_greet  
* requirement_concours{"requirement":"conditions", "concoursAll":"direct b"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## require27  
* requirement_concours{"requirement":"conditions", "concoursAll":"direct b"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require28
* greet
  - utter_greet  
* requirement_concours{"requirement":"conditions", "concoursAll":"direct b"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require29  
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel a"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## require30
* greet
  - utter_greet  
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel a"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## require31  
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel a"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require32
* greet
  - utter_greet  
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel a"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require33 
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel b"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## require34
* greet
  - utter_greet 
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel b"}
  - action_require
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## require35 
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel b"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
* concours_inscriptioon{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require36
* greet
  - utter_greet 
* requirement_concours{"requirement":"conditions", "concoursAll":"professionnel b"}
  - action_require
* pay_concours{"pay":"frais"}
  - action_pay
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


## admissions
* admissibilite{"admis": "admissibilité"}
  - slot{"admis": "admissibilité"}
  - utter_process_status
  - admissibilite_form
  - form{"name": "admissibilite_form"}
  - slot{"requested_slot": "num"}
* admissibilite
  - admissibilite_form
* admissibilite
  - admissibilite_form
  - form{"name": null}  

  