from Relation import *
from Personne import *

tableauRelations = set()
tableauIndividus = set()


#TODO :

#  fonction : creerReseauSocial( , ) :
#   Lire les fichiers texte contenant les informations
#   et genere le reseau social correspondant.
def creerReseauSocial(fichier1, fichier2):
    individus = open(fichier1, "r")
    relations = open(fichier2, "r")
    for ligne in individus:
        personne = ligne.split(" ")
        tableauIndividus.add(Personne(personne[0], personne[1], personne[2], personne[3]))
    for ligne in relations:  
        chaines = ligne.split(" ")
        if int(chaines[1]) > 0 and int(chaines[1]) <= 100:
            tableauRelations.add(Relations(chaines[0], chaines[2], int(chaines[1])))

#
#  fonction : afficherReseauSocial()
#   Affiche le réseau social selon le format présenté en annexe.
def afficherReseauSocial():
    #creerReseauSocial("individus.txt","Relations.txt")
    if len(tableauRelations) == 0:
        print("Aucun Reseau Trouver!\n")
        return
    for relation in tableauRelations:
        print("(%s,%s(%s%%))\n" % (relation.nomIndividu1.strip(), relation.nomIndividu2.strip(), str(relation.facteurRelations).strip()))

caracteristiquesCheveux = ["N", "R", "B", "M"]

lesQuestionsCheveux = ["Les individues mysteres ont-ils les cheveux noirs-N ? ",
                    "Les individues mysteres ont-ils les cheveux roux-R ? ",
                    "Les individues mysteres ont-ils les cheveux blonds-B ? ",
                    "Les individues mysteres ont-ils les cheveux marrons-M ? "]

caracteristiquesYeux = ["B", "V", "N", "G", "M"]

lesQuestionsYeux = ["Les individues mysteres ont-ils les yeux bleus-B ? ",
                    "Les individues mysteres ont-ils les yeux verts-V ? ",
                    "Les individues mysteres ont-ils les yeux noirs-N ? ",
                    "Les individues mysteres ont-ils les yeux gris-G ? ",
                    "Les individues mysteres ont-ils les yeux marrons-M ? "]

# on n'a pas utiliser les caracteristique
caracteristiquesGenie = ["GI", "GP", "GE",
                        "GC", "GA", "GM", "GB", "GInd", "ER"]

lesQuestionsGenies = [" Les individus sont-ils en génie informatique-GI ?",
                    " Les individus sont-ils en génie physique-GP ?",
                    " Les individus sont-ils en génie electrique-GE ?",
                    " Les individus sont-ils en génie chimique-GC ?",
                    " Les individus sont-ils en génie aerospatial-GA ?",
                    " Les individus sont-ils en génie mecanique-GM ?",
                    " Les individus sont-ils en génie biomédical-GB ?",
                    " Les individus sont-ils en génie industriel-GInd ?",
                    " Les individus sont-ils en génie énergétique-ER ?"]

compteurQuestionsPosees = [0, 0, 0, 0]
compteurU = [0, 0, 0]
# !! pour se rappeller des reponses des questions le max est 6 pas sur de la declaration
conteneurReponse = [None, None, None, None, None, None]
tableauIndividusEvolutif = set()

# Decoupage de la fonction identifierIndividus() :
# Questions a poser (compteur locale)
#Questions pour cheveux :

def suspects(tableau) : 
    print("Les suspects sont :")
    for personne in tableau :
        print(personne.nom)

# on doit posé la question une par une puis agir en cosequence de la reponse
#parce que la on a les reponses sans qu'on pose les questions
#j'ai pensé qu'il nous faut deux valeures car on peut avoir deux solution en cas d'une reponse avec u
# je pense qu'on peut mettre ce bool comme une condition pour la question des yeux
def questionsCheveux():
    indexQuestionsCheveux = 0
    while compteurU[0] < 2:
        reponseCheveux = input(lesQuestionsCheveux[indexQuestionsCheveux])
        while reponseCheveux.upper() not in ["O","N","U","S"]:
            reponseCheveux = input(lesQuestionsCheveux[indexQuestionsCheveux])
        if reponseCheveux.upper() == "S" : 
            suspects(tableauIndividusEvolutif)
        elif reponseCheveux.upper() == "O" :
            conteneurReponse[0] = caracteristiquesCheveux[indexQuestionsCheveux]
            conteneurReponse[1] = "vide"
            compteurU[0] = 2
            break
        elif reponseCheveux.upper() == "U" :
            compteurU[0] += 1
            conteneurReponse[compteurU[0] - 1] = caracteristiquesCheveux[indexQuestionsCheveux]
        elif (reponseCheveux.upper() == "O") or (reponseCheveux.upper() == "U"): #???
            for personne in tableauIndividus:
                 if personne.cheveux == caracteristiquesCheveux[indexQuestionsCheveux]:
                    tableauIndividusEvolutif.add(personne)
        indexQuestionsCheveux += 1
    compteurQuestionsPosees[0] = indexQuestionsCheveux+1
    return


def questionsYeux():
    indexQuestionsYeux = 0
    while compteurU[1] < 2:
        reponseYeux = input(lesQuestionsYeux[indexQuestionsYeux])
        while reponseYeux.upper() not in ["O", "U", "N", "S"]:
            reponseYeux = input(lesQuestionsYeux[indexQuestionsYeux])
        if (reponseYeux.upper() == "S"): 
            suspects(tableauIndividusEvolutif)
        elif(reponseYeux.upper() == "O"):
            conteneurReponse[2] = caracteristiquesYeux[indexQuestionsYeux]
            conteneurReponse[3] = "vide"
            compteurU[1] = 2
            break
        elif reponseYeux.upper() == "U":
            compteurU[1] += 1
            conteneurReponse[compteurU[1] + 1] = caracteristiquesYeux[indexQuestionsYeux]
        elif reponseYeux.upper() == "N":
            for personne in tableauIndividusEvolutif:
                if personne.yeux == caracteristiquesYeux[indexQuestionsYeux]:
                    del(personne)
        indexQuestionsYeux += 1
    compteurQuestionsPosees[1] = indexQuestionsYeux + 1
    return


def questionsGenie():
    indexQuestionsGenie = 0
    while compteurU[2] < 2:
        reponseGenie = input(lesQuestionsGenies[indexQuestionsGenie])
        while reponseGenie.upper() not in ["O", "U", "N", "S"]:
            reponseGenie = input(lesQuestionsGenies[indexQuestionsGenie])
        if reponseGenie.upper() == "S": 
            suspects(tableauIndividusEvolutif) 
        elif reponseGenie.upper() == "O":
            conteneurReponse[4] = caracteristiquesYeux[indexQuestionsGenie]
            conteneurReponse[5] = "vide"
            compteurU[2] = 2
            break
        elif reponseGenie.upper() == "U":
            compteurU[2] += 1
            conteneurReponse[compteurU[1] + 3] = caracteristiquesGenie[indexQuestionsGenie]
        elif reponseGenie.upper() == "N":
            for personne in tableauIndividusEvolutif:
                if personne.genie == caracteristiquesGenie[indexQuestionsGenie]:
                    del(personne)
        indexQuestionsGenie += 1
    compteurQuestionsPosees[2] = indexQuestionsGenie + 1
    return

tableauIndividusFinale = set()
#  fonction : identifierIndividus()
#   l'agent trouve les noms des deux individues mystères.
def identifierIndividus() : 
    tableauIndividusFiltre = set() 
    questionsCheveux()
    questionsYeux()
    questionsGenie()
    if len(tableauIndividusEvolutif) == 2 : 
        print("Les individues mysteres sont: ", tableauIndividusEvolutif.copy(0, 0).name, " et ", tableauIndividusEvolutif.copy(1, 1).name)
    else : 
        index = 0
        personnesTrouvees = False
        compteurU = 0  
        while (personnesTrouvees and compteurU < 2) :
            reponsePersonnes = input("Les personnes suspectes sont-ils ", tableauIndividusEvolutif.copy(index, index).name, tableauIndividusEvolutif.copy(index+1, index+1).name)
            while reponsePersonnes.upper() not in ["O", "N", "U", "S"]:
                reponsePersonnes = input("Les personnes suspectes sont-ils ", tableauIndividusEvolutif.copy(index, index).name , tableauIndividusEvolutif.copy(index+1,index+1).name)
            if reponsePersonnes.upper() == "S" : 
                suspects(tableauIndividusFiltre)
            else :
                if reponsePersonnes.upper() == "O" : 
                    personnesTrouvees = True 
                    tableauIndividusFinale.add(tableauIndividusEvolutif.copy(index,index))
                    tableauIndividusFinale.add(tableauIndividusEvolutif.copy(index+1,index+1))
                if reponsePersonnes.upper() == "U" :
                    compteurU = compteurU + 1 
                    tableauIndividusFiltre.add(tableauIndividusEvolutif.copy(index,index))
                    tableauIndividusFiltre.add(tableauIndividusEvolutif.copy(index+1, index+1))
            compteurQuestionsPosees[3] = compteurQuestionsPosees[3] + 1 
            index =+ 2 
            if len(tableauIndividusFiltre) > 2  :
                reponsePersonnesFiltre = input("Les personnes suspectes sont-ils ", tableauIndividusFiltre.copy(0, 0).name, tableauIndividusFiltre.copy(2, 2).name)
                while reponsePersonnesFiltre.upper() not in ["O", "N", "U", "S"]:
                    reponsePersonnesFiltre = input("Les personnes suspectes sont-ils ", tableauIndividusEvolutif.copy(0, 0).name, tableauIndividusEvolutif.copy(2, 2).name)
                if reponsePersonnesFiltre.upper() == "S" : 
                    suspects(tableauIndividusFiltre)
                if reponsePersonnesFiltre.upper() == "O" : 
                    tableauIndividusFinale.add(tableauIndividusFiltre.copy(0, 0))
                    tableauIndividusFinale.add(tableauIndividusFiltre.copy(2, 2))
                if reponsePersonnesFiltre.upper() == "U" :
                    reponsePersonnesFiltre2 = input("Les personnes suspectes sont-ils ", tableauIndividusFiltre.copy(0, 0).name, tableauIndividusFiltre.copy(3, 3).name)
                    while reponsePersonnesFiltre2.upper() not in ["O", "N",  "S"]:
                        reponsePersonnesFiltre2 = input("Les personnes suspectes sont-ils ", tableauIndividusFiltre.copy(0, 0).name, tableauIndividusFiltre.copy(3, 3).name)
                    if reponsePersonnesFiltre2.upper() == "S":
                        suspects(tableauIndividusFiltre)
                    if reponsePersonnesFiltre2 == "O" : 
                        tableauIndividusFinale.add(tableauIndividusFiltre.copy(0,0))
                        tableauIndividusFinale.add(tableauIndividusFiltre.copy(3,3))
                    else : 
                        tableauIndividusFinale.add(tableauIndividusFiltre.copy(1, 1))
                        tableauIndividusFinale.add(tableauIndividusFiltre.copy(2, 2))


#
#  fonction : enleverArcsIndesirables( 3 caracteristiques indesirables )
#   Génère le sous-graphe des caractéristiques désirables.
def get(nom):
    for personnes in tableauIndividus:
        if personnes.nom == nom : 
            return personnes

def enleverArcsIndesirables(cheveux , yeux , genie ) :
    for relations in tableauRelations : 
        if not (get(relations.nomIndividu1).cheveux == get(relations.nomIndividu2).cheveux or get(relations.nomIndividu1).yeux == get(relations.nomIndividu2).yeux or get(relations.nomIndividu1).genie == get(relations.nomIndividu2).genie) :
            relations.facteurRelations = 0 


#  fonction : trouverChaineContacts( 2 noms d'individus )

#TODO with Dijksta algorithm !!

#   L'agent trouve la meilleure chaine de contacts entre 2 individus à partir 
#   du sous-graphe des caracteristiques désirables.

def trouverChaineContacts(nomSource , nomCible) :  
    return
#  fontion : afficherResultat() 
#   L'agent présente le résultatde ses accomplissements selon le bon format.
def afficherResultat() :
    for relation in tableauRelations:
        if relation.facteurRelations != 0:
            print("(%s,%s(%s%%))\n" % (relation.nomIndividu1.strip(), relation.nomIndividu2.strip(), str(relation.facteurRelations).strip())) 
    #Show path
    print("Nombre de questions posees: ", compteurQuestionsPosees[0] + compteurQuestionsPosees[1] + compteurQuestionsPosees[2] + compteurQuestionsPosees[3],"\n")
    print()
    print()
    print()
        
    return
# Interface console qui affiche le menu : 
#   a/ Créer le résea social.
#   b/ Afficher le réseau social.
#   c/ Jouer à Qui est-ce ? 
#   d/ Afficher le résultat.
#   e/ Quitter. 
#
########################

def lireInput() :
    valeur = input()
    if valeur.lower() not in ["a","b","c","d","e"]:
        print("Index Invalide, reessayez:\n")
        valeur = "m"
    return valeur.lower()

# main 
def main() :
    current = "m"
    #Menu
    while True:
        if current == "m":
            print("a/ Créer le résea social.")
            print("b/ Afficher le réseau social.")
            print("c/ Jouer à Qui est-ce ?")
            print("d/ Afficher le résultat.")
            print("e/ Quitter")
            current = lireInput()
        elif current == "a":
            creerReseauSocial("Individus.txt", "Relations.txt")
            current = "m"
        elif current == "b":
            afficherReseauSocial()
            current = "m"
        elif current == "c":
            identifierIndividus()
            current = "m"
        elif current == "d":
            afficherResultat()
            current = "m"
        elif current == "e":
            break

if __name__== "__main__":
    main()
