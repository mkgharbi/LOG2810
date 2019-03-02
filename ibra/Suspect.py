########################
from reseauSocial import *

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
                    "Les individues mysteres ont-ils les yeux marrons-M ? ", ]


caracteristiquesGenie = ["GI", "GP", "GE",
                        "GC", "GA", "GM", "GB", "GInd", "ER"]

lesQuestionsGenies = [" Les individus sont-ils en génie informatique-GI ?"
                    " Les individus sont-ils en génie physique-GP ?"
                    " Les individus sont-ils en génie electrique-GE ?"
                    " Les individus sont-ils en génie chimique-GC ?"
                    " Les individus sont-ils en génie aerospatial-GA ?"
                    " Les individus sont-ils en génie mecanique-GM ?"
                    " Les individus sont-ils en génie biomédical-GB ?"
                    " Les individus sont-ils en génie industriel-GInd ?"
                    " Les individus sont-ils en génie énergétique-ER ?"]

compteurQuestionsPosees = [0, 0, 0, 0]
compteurU = [0, 0, 0]
# pour se rappeller des reponses des questions le max est 6 
conteneurReponse = [""]
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
    passerQuestionCheveux = False
    indexQuestionsCheveux = 0
    while compteurU[0] < 2 or passerQuestionCheveux:
        reponseCheveux = input(lesQuestionsCheveux[indexQuestionsCheveux])
        while reponseCheveux.upper() not in ["O", "N", "U" , "S"]:
            reponseCheveux = input(lesQuestionsCheveux[indexQuestionsCheveux])
        if reponseCheveux.upper() == "S" : 
            suspects(tableauIndividusEvolutif)
        else :
            if (reponseCheveux.upper() == "O"):
                passerQuestionCheveux = True
                conteneurReponse[0] = caracteristiquesCheveux[indexQuestionsCheveux]
                conteneurReponse[1] = "vide"
            if (reponseCheveux.upper() == "U"):
                compteurU[0] = + 1
                conteneurReponse[compteurU[0] - 1] = caracteristiquesCheveux[indexQuestionsCheveux]
            if (reponseCheveux.upper() == "O") or (reponseCheveux.upper() == "U"):
                for personne in tableauIndividus: 
                    if personne.cheveux == caracteristiquesCheveux[indexQuestionsCheveux]:
                        tableauIndividusEvolutif.add(personne)
            indexQuestionsCheveux += 1
    compteurQuestionsPosees[0] = indexQuestionsCheveux+1
    return


def questionsYeux():
    passerQuestionYeux = False
    indexQuestionsYeux = 0
    while compteurU[1] < 2 or passerQuestionYeux:
        reponseYeux = input(lesQuestionsYeux[indexQuestionsYeux])
        while reponseYeux.upper() not in ["O", "U", "N", "S"]:
            reponseYeux = input(lesQuestionsYeux[indexQuestionsYeux])
        if (reponseYeux.upper() == "S"): 
            suspects(tableauIndividusEvolutif)
        else : 
            if (reponseYeux.upper() == "O"):
                passerQuestionYeux = True
                conteneurReponse[2] = caracteristiquesYeux[indexQuestionsYeux]
                conteneurReponse[3] = "vide"
            if reponseYeux.upper() == "U":
                compteurU[1] = + 1
                conteneurReponse[compteurU[1] + 1] = caracteristiquesYeux[indexQuestionsYeux]
            if reponseYeux.upper() == "N":
                for personne in tableauIndividusEvolutif:
                    if personne.yeux == caracteristiquesYeux[indexQuestionsYeux]:
                        del(personne)
            indexQuestionsYeux = + 1
    compteurQuestionsPosees[1] = indexQuestionsYeux + 1
    return


def questionsGenie():
    passerQuestionGenie = False
    indexQuestionsGenie = 0
    while compteurU[1] < 2 or passerQuestionGenie:
        reponseGenie = input(lesQuestionsGenies[indexQuestionsGenie])
        while reponseGenie.upper() not in ["O", "U", "N", "S"]:
            reponseGenie = input(lesQuestionsGenies[indexQuestionsGenie])
        if reponseGenie.upper() == "S" : 
            suspects(tableauIndividusEvolutif)
        else : 
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

    return

