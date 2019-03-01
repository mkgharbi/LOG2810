
########################


#Classe : 
class Personne :
    
    def _init_(self, nom, couleurDeCheveux, couleurDesYeux, genie) :
        self.nom = nom
        self.couleurDeCheveux = couleurDeCheveux
        self.couleurDesYeux = couleurDesYeux
        self.genie = genie

tableauRelations =  {} 
tableauIndividus = {}


#TODO : 

#  fontion : creerReseauSocial( , ) : 
#   Lire les fichiers texte contenant les informations 
#   et genere le reseau social correspondant. 
def creerReseauSocial(fichier1 , fichier2) : 
    individus = open(fichier1,"r")
    relations = open(fichier2 , "r")
    for ind in individus : 
        personne = ind.split(" ")
        tableauIndividus.add(Personne(personne[0], personne[1], personne[2] ,personne[3] ))
    for lignes in relations :  # A verifier 
        chaines = lignes.split(" ")
        if chaines[1] > 0 and chaines[1] <=100 :
            tableauRelations.add(" ( " + chaines[0] + "  " + chaines[2] + "  ( " + chaines[1] + "%") 
            

#
#  fonction : afficherReseauSocial() 
#   Affiche le réseau social selon le format présenté en annexe. 
def afficherReseauSocial() :
    for x in tableauRelations : 
        print(tableauRelations[x])
# 


caracteristiquesCheveux = ["N", "R", "B", "M"]

lesQuestionsCheveux = ["Les individues mysteres ont-ils les cheveux noirs-N ? ",
                    "Les individues mysteres ont-ils les cheveux roux-R ? " , 
                    "Les individues mysteres ont-ils les cheveux blonds-B ? " , 
                    "Les individues mysteres ont-ils les cheveux marrons-M ? " ]

caracteristiquesYeux = [ "B" , "V" , "N" , "G" , "M" ]

lesQuestionsYeux = [   "Les individues mysteres ont-ils les yeux bleus-B ? " , 
                    "Les individues mysteres ont-ils les yeux verts-V ? " , 
                    "Les individues mysteres ont-ils les yeux noirs-N ? " ,
                    "Les individues mysteres ont-ils les yeux gris-G ? " , 
                    "Les individues mysteres ont-ils les yeux marrons-M ? ",  ]

caracteristiquesGenie = ["GI" , "GP" , "GE" , "GC" , "GA" , "GM" , "GB" , "GInd" , "ER"] # on n'a pas utiliser les caracteristique 

lesQuestionsGenies = [ " Les individus sont-ils en génie informatique-GI ?"
                    " Les individus sont-ils en génie physique-GP ?"
                    " Les individus sont-ils en génie electrique-GE ?"
                    " Les individus sont-ils en génie chimique-GC ?"
                    " Les individus sont-ils en génie aerospatial-GA ?"
                    " Les individus sont-ils en génie mecanique-GM ?"
                    " Les individus sont-ils en génie biomédical-GB ?"
                    " Les individus sont-ils en génie industriel-GInd ?"
                    " Les individus sont-ils en génie énergétique-ER ?"]

compteurQuestionsPosees = [0 , 0 , 0 ]
compteurU = [0 , 0 , 0 ]
conteneurReponse = [""]  # !! pour se rappeller des reponses des questions le max est 6 pas sur de la declaration 
tableauIndividusEvolutif = set()

# Decoupage de la fonction identifierIndividus() : 
# Questions a poser (compteur locale)
#Questions pour cheveux :



# on doit posé la question une par une puis agir en cosequence de la reponse 
#parce que la on a les reponses sans qu'on pose les questions 
#j'ai pensé qu'il nous faut deux valeures car on peut avoir deux solution en cas d'une reponse avec u 
# je pense qu'on peut mettre ce bool comme une condition pour la question des yeux
def questionsCheveux() :
    passerQuestionCheveux = False
    indexQuestionsCheveux = 0 
    while compteurU[0] < 2 or passerQuestionCheveux:
        reponseCheveux = input(lesQuestionsCheveux[indexQuestionsCheveux])
        while reponseCheveux.upper() not in ["O", "N", "U"]:
            reponseCheveux = input(lesQuestionsCheveux[indexQuestionsCheveux])
        if (reponseCheveux.upper() == "O") : 
            passerQuestionCheveux = True 
            conteneurReponse[0] = caracteristiquesCheveux[indexQuestionsCheveux]
            conteneurReponse[1] = "vide"
        if (reponseCheveux.upper() == "U"):
            compteurU[0] =+ 1 
            conteneurReponse[compteurU[0] -1] = caracteristiquesCheveux[indexQuestionsCheveux]
        if (reponseCheveux.upper() == "O") or (reponseCheveux.upper() == "U") :
            for personne in tableauIndividus: 
                if personne.cheveux == caracteristiquesCheveux[indexQuestionsCheveux]:
                    tableauIndividusEvolutif.add(personne)
        indexQuestionsCheveux += 1
    compteurQuestionsPosees[0] = indexQuestionsCheveux+1 
    return 



def questionsYeux () : 
    passerQuestionYeux = False 
    indexQuestionsYeux = 0 
    while compteurU[1] < 2 or passerQuestionYeux :
        reponseYeux = input(lesQuestionsYeux[indexQuestionsYeux])
        while reponseYeux.upper() not in ["O","U","N"]:
            reponseYeux = input(lesQuestionsYeux[indexQuestionsYeux])
        if (reponseYeux.upper() == "O") : 
            passerQuestionYeux = True 
            conteneurReponse[2] = caracteristiquesYeux[indexQuestionsYeux]
            conteneurReponse[3] = "vide"
        if reponseYeux.upper() == "U" : 
            compteurU[1] =+ 1 
            conteneurReponse[compteurU[1] + 1] = caracteristiquesYeux[indexQuestionsYeux]
        if reponseYeux.upper() == "N" :
            for personne in tableauIndividusEvolutif : 
                if personne.yeux == caracteristiquesYeux[indexQuestionsYeux] : 
                    del(personne)
        indexQuestionsYeux =+ 1 
    compteurQuestionsPosees[1] = indexQuestionsYeux + 1
    return 

def questionsGenie() : 
    passerQuestionGenie = False
    indexQuestionsGenie = 0
    while compteurU[1] < 2 or passerQuestionGenie:
        reponseGenie = input(lesQuestionsGenies[indexQuestionsGenie])
        while reponseGenie.upper() not in ["O", "U", "N"]:
            reponseGenie = input(lesQuestionsGenies[indexQuestionsGenie])
        if (reponseGenie.upper() == "O"):
            passerQuestionGenie = True
            conteneurReponse[4] = caracteristiquesYeux[indexQuestionsGenie]
            conteneurReponse[5] = "vide"
        if reponseGenie.upper() == "U":
            compteurU[2] = + 1
            conteneurReponse[compteurU[1] + 3] = caracteristiquesGenie[indexQuestionsGenie]
        if reponseGenie.upper() == "N":
            for personne in tableauIndividusEvolutif:
                if personne.genie == caracteristiquesGenie[indexQuestionsGenie]:
                    del(personne)
        indexQuestionsGenie = + 1
    compteurQuestionsPosees[2] = indexQuestionsGenie + 1
    return





passerQuestionSuivanteCheveux = False ## je pense qu'on peut mettre ce bool comme une condition pour la question des yeux
def questionsCheveux(reponse, valeur1, valeur2):
    if reponse == "o" or reponse == "u" :
        conteneurReponse[0] = valeur1
        conteneurReponse[1] = valeur2
        for personnes in tableauIndividus :
            if personnes.couleurDeCheveux == valeur1 or personnes.couleurDeCheveux == valeur2 :
                tableauIndividusEvolutif.add(personnes)
        if reponse == "u" :
            compteurU[0] = compteurU[0] + 1
         #   if compteurU[0] = 2 :
          #      passerQuestionSuivanteCheveux = True 
        else :
            passerQuestionSuivanteCheveux = True
    compteurQuestionsPosees[0] = compteurQuestionsPosees[0]+1
########################################################
##def questionsCheveux(reponse, valeur ):
  ##  if reponse == "o" or reponse == "u":
    ##    for personnes in tableauIndividus : 
      ##      if personnes.couleurDeCheveux == valeur :
        ##        tableauIndividusEvolutif.add(personnes)
     ##   if reponse == " u " :
       ##     compteurU[0] = compteurU[0] + 1 
       ## else : 
         ##   passerQuestionSuivanteCheveux = true 
    ##compteurQuestionsPosees[0] = compteurQuestionsPosees[0]+1

#Questions pour yeux : 
passerQuestionSuivanteYeux = False

def questionsYeux(reponse, valeur1, valeur2):
    if reponse == "o" or reponse == "u" :
        conteneurReponse[2]= valeur1
        conteneurReponse[3]= valeur2
        for personnes in tableauIndividus:
            #je me demande si je met un autre if pour la couleur des yeux qui sera dans le if de couleur des cheveux 
            if (personnes.couleurDeCheveux == conteneurReponse[0] or personnes.couleurDeCheveux == conteneurReponse[1]) and (personnes.couleurDesYeux == valeur1 or personnes.couleurDesYeux == valeur2):
                tableauIndividusEvolutif.add(personnes)    
                #faire une relecture sur le tableau evolutif pour supprimer ceux qui non pas la meme couleur de yeux 
                for i in tableauIndividusEvolutif:
                    if i.couleurDesYeux != valeur1 or i.couleurDesYeux!= valeur2:
                        del(tableauIndividusEvolutif[i])  
        if reponse == "u":
            compteurU[1] = compteurU[1]+1
          #  if compteurU[1]==2 :
           #     passerQuestionSuivanteYeux= True     
        else:
            passerQuestionSuivanteYeux = True
    compteurQuestionsPosees[1] = compteurQuestionsPosees[1]+1           



# def questionsYeux(reponse, valeur):
#    if reponse == "o" or reponse == "u" and valeur:
#        for personnes in tableauIndividus:
#            if personnes.couleurDesYeux == valeur:
#                tableauIndividusEvolutif.add(personnes)
#        if reponse == " u ":
#            compteurU[1] = compteurU[1] + 1
#        else:
 #           passerQuestionSuivanteYeux = true
 #   compteurQuestionsPosees[1] = compteurQuestionsPosees[1]+1

#Questions pour genie :
passerQuestionSuivanteGenie = False
# a faire comme pour la couleur des yeux 
def questionsGenie(reponse, valeur):
    if reponse == "o" or reponse == "u":
        for personnes in tableauIndividus:
            if personnes.genie == valeur:
                tableauIndividusEvolutif.add(personnes)
        if reponse == " u ":
            compteurU[2] = compteurU[2] + 1
        else:
            passerQuestionSuivanteGenie = true
    compteurQuestionsPosees[2] = compteurQuestionsPosees[2]+1



def questions () : 
    indexQuestionsCheveux = 0 
    while compteurU[0] < 2 or passerQuestionSuivanteCheveux:
        reponseCheveux = input(lesQuestionsCheveux[indexQuestionsCheveux])
        while reponseCheveux.upper() not in ["O", "N", "U"]:
            reponseCheveux = input(lesQuestionsCheveux[indexQuestionsCheveux])
        questionsCheveux(reponseCheveux , caracteristiquesCheveux[indexQuestionsCheveux])
        indexQuestionsCheveux += 1
    
    indexQuestionsYeux = 0 
    while compteurU[1] < 2 or passerQuestionSuivanteYeux : 
        reponseYeux = input(lesQuestionsYeux[indexQuestionsYeux])
        while reponseYeux.upper() not in ["O", "N", "U"]:
            reponseYeux = input(lesQuestionsYeux[indexQuestionsYeux])
        questionsYeux(reponseYeux ,caracteristiquesYeux[indexQuestionsYeux])
        indexQuestionsYeux += 1
    
    indexQuestionsGenie = 0 
    while compteurU[2] < 2 or passerQuestionSuivanteGenie : 
        reponseGenie = input(lesQuestionsGenie[indexQuestionsGenie])
        while ( reponseGenie.upper() != "O" and reponseGenie.upper() != "N" and reponseGenie.upper() != "U") :
            reponseGenie = input(lesQuestionsGenie[indexQuestionsGenie])
        questionsGenie(reponseGenie, caracteristiquesGenie[indexQuestionsGenie])
        indexQuestionsGenie += 1
    

#  fonction : identifierIndividus()
#   l'agent trouve les noms des deux individues mystères.
def identifierIndividus() : 
    return
#
#  fonction : enleverArcsIndesirables( 3 caracteristiques indesirables )
#   Génère le sous-graphe des caractéristiques désirables.
def enleverArcsIndesirables() :
    return
#  fonction : trouverChaineContacts( 2 noms d'individus )
#   L'agent trouve la meilleure chaine de contacts entre 2 individus à partir 
#   du sous-graphe des caracteristiques désirables.

def trouverChaineContacts() :  
    return
#  fontion : afficherResultat() 
#   L'agent présente le résultatde ses accomplissements selon le bon format.
def afficherResultat() :
    return
# Interface console qui affiche le menu : 
#   a/ Créer le résea social.
#   b/ Afficher le réseau social.
#   c/ Jouer à Qui est-ce ? 
#   d/ Afficher le résultat.
#   e/ Quitter. 
#
########################

#selections = {
 #   0:"afficherMenu",
  #  1:"a",
   # 2:"b",
    #3:"c",
#    4:"d",
 #   5:"e",
#}

#def lireInput() :
  #  valeur = None
   # while valeur not in ["a","b","c","d","e"]:
   ##     valeur = input()
   # return valeur

# main 
#def main() :
   ## current = selections[0]
    #Menu
   # while True:
      #  if current == "afficherMenu":
    #        print("a/ Créer le résea social.")
      #      print("b/ Afficher le réseau social.")
     ##       print("c/ Jouer à Qui est-ce ?")
       #     print("d/ Afficher le résultat.")
        #    print("e/ Quitter")
         #   current = lireInput()
        #elif current == "a":
        #    creerReseauSocial("Individus.txt", "Relations.txt")
         #   current = selections[0]
        #elif current == "b":
         #   afficherReseauSocial()
          #  current = selections[0]
        #elif current == "c":
            #questions()
         #   current = selections[0]
        ##elif current == "d":
          #  afficherResultat()
           # current = selections[0]
        #elif current == "e":
         #   break

#if __name__== "__main__":
 # main()
