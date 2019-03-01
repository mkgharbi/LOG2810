
########################


#Classe : 
class Personne :
    
    def _init_(self, nom, couleurDeCheveux, couleurDesYeux, genie) :
        self.nom = nom
        self.couleurDeCheveux = couleurDeCheveux
        self.couleurDesYeux = couleurDesYeux
        self.genie = genie
        self.nombreLiens = 0  


#TODO :
    tableauRelations = {}
    tableauIndividus = {}
#  fontion : creerReseauSocial( , ) : 
#   Lire les fichiers texte contenant les informations 
#   et genere le reseau social correspondant. 
def creerReseauSocial(fichier1 , fichier2) : 
    individus = open(fichier1,"r")
    relations = open(fichier2 , "r")
    for ind in individus : 
        personne = ind.split(" ")
        tableauIndividus.add(Personne(personne[0], personne[1], personne[2] ,personne[3]))
    for lignes in relations :   
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


tableauCaracteristiquesCheveux = ["N", "R", "B", "M"]

tableauquestionsCheveux = ["Les individues mysteres ont-ils les cheveux noirs-N ? ",
                    "Les individues mysteres ont-ils les cheveux roux-R ? " , 
                    "Les individues mysteres ont-ils les cheveux blonds-B ? " , 
                    "Les individues mysteres ont-ils les cheveux marrons-M ? " ]

tableauCaracteristiquesYeux = [ "B" , "V" , "N" , "G" , "M" ]

tableauQuestionsYeux = [   "Les individues mysteres ont-ils les yeux bleus-B ? " , 
                    "Les individues mysteres ont-ils les yeux verts-V ? " , 
                    "Les individues mysteres ont-ils les yeux noirs-N ? " ,
                    "Les individues mysteres ont-ils les yeux gris-G ? " , 
                    "Les individues mysteres ont-ils les yeux marrons-M ? ",  ]

tableauCaracteristiquesGenie = ["GI" , "GP" , "GE" , "GC" , "GA" , "GM" , "GB" , "GInd" , "ER"]

tableauQuestionsGenies = [ " Les individus sont-ils en génie informatique-GI ?"
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
tableauIndividusEvolutif = {}

# Decoupage de la fonction identifierIndividus() : 
# Questions a poser (compteur locale)
#Questions pour cheveux :


def questionsCheveux(reponse, valeur, passerQuestionSuivanteCheveux):
    if reponse == "o" or reponse == "u":
        for personnes in tableauIndividus : 
            if personnes.couleurDesCheveux == valeur :
                tableauIndividusEvolutif.add(personnes)
        if reponse == " u " :
            compteurU[0] = compteurU[0] + 1 
        else : 
            passerQuestionSuivanteCheveux = true 
    compteurQuestionsPosees[0] = compteurQuestionsPosees[0]+1

#Questions pour yeux : 


def questionsYeux(reponse, valeur, passerQuestionSuivanteYeux):
    if reponse == "o" or reponse == "u":
        for personnes in tableauIndividus:
            if personnes.couleurDesYeux == valeur:
                tableauIndividusEvolutif.add(personnes)
        if reponse == " u ":
            compteurU[1] = compteurU[1] + 1
        else:
            passerQuestionSuivanteYeux = true
    compteurQuestionsPosees[1] = compteurQuestionsPosees[1]+1

#Questions pour genie :


def questionsGenie(reponse, valeur, passerQuestionSuivanteGenie):
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
    passerQuestionSuivanteCheveux = False

    while compteurU[0] < 2 or passerQuestionSuivanteCheveux:
        reponseCheveux = input(tableauQuestionsCheveux[indexQuestionsCheveux])
        while ( reponseCheveux.upper() != "O" and reponseCheveux.upper() != "N"  and reponseCheveux.upper() != "U") :
            reponseCheveux = input(tableauQuestionsCheveux[indexQuestionsCheveux])
        questionsCheveux(
            reponseCheveux, tableauCaracteristiquesCheveux[indexQuestionsCheveux], passerQuestionSuivanteCheveux)
        indexQuestionsCheveux += 1
    
    passerQuestionSuivanteYeux = False

    indexQuestionsYeux = 0 
    while compteurU[1] < 2 or passerQuestionSuivanteYeux : 
        reponseYeux = input(tableauQuestionsYeux[indexQuestionsYeux])
        while ( reponseYeux.upper() != "O" and reponseYeux.upper() != "N" and reponseYeux.upper() != "U") :
            reponseYeux = input(tableauQuestionsYeux[indexQuestionsYeux])
        questionsYeux(reponseYeux, tableauCaracteristiquesYeux[indexQuestionsYeux], passerQuestionSuivanteYeux)
        indexQuestionsYeux += 1
    

    passerQuestionSuivanteGenie = False
    indexQuestionsGenie = 0 
    while compteurU[2] < 2 or passerQuestionSuivanteGenie : 
        reponseGenie = input(tableauQuestionsGenie[indexQuestionsGenie])
        while ( reponseGenie.upper() != "O" and reponseGenie.upper() != "N" and reponseGenie.upper() != "U") :
            reponseGenie = input(tableauQuestionsGenie[indexQuestionsGenie])
        questionsGenie(
            reponseGenie, tableauCaracteristiquesGenie[indexQuestionsGenie], passerQuestionSuivanteGenie)
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

#TODO with Dijksta algorithm !!

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

selections = {
    0:"afficherMenu",
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
}

def lireInput() :
    valeur = None
    while valeur not in ["a","b","c","d","e"]:
        valeur = input()
    return valeur

# main 
def main() :
    current = selections[0]
    #Menu
    while True:
        if current == "afficherMenu":
            print("a/ Créer le résea social.")
            print("b/ Afficher le réseau social.")
            print("c/ Jouer à Qui est-ce ?")
            print("d/ Afficher le résultat.")
            print("e/ Quitter")
            current = lireInput()
        elif current == "a":
            creerReseauSocial("Individus.txt", "Relations.txt")
            current = selections[0]
        elif current == "b":
            afficherReseauSocial()
            current = selections[0]
        elif current == "c":
            #questions()
            current = selections[0]
        elif current == "d":
            afficherResultat()
            current = selections[0]
        elif current == "e":
            break

if __name__== "__main__":
    main()
