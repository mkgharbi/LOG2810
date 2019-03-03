########################
import collections

#Classe :
class Personne:

    def __init__(self, nom, couleurDeCheveux, couleurDesYeux, genie):
        self.nom = nom
        self.couleurDeCheveux = couleurDeCheveux
        self.couleurDesYeux = couleurDesYeux
        self.genie = genie
    def __str__(self):
        return 



class Relations: 
    def __init__(self, nomIndividu1 , nomIndividu2, facteurRelations):
        self.nomIndividu1 = nomIndividu1
        self.nomIndividu2 = nomIndividu2
        self.facteurRelations = facteurRelations


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
        tableauIndividus.add(Personne(personne[0].strip(), personne[1].strip(), personne[2].strip(), personne[3].strip()))
    for ligne in relations:  
        chaines = ligne.split(" ")
        if int(chaines[1]) > 0 and int(chaines[1]) <= 100:
            tableauRelations.add(Relations(chaines[0].strip(), chaines[2].strip(), int(chaines[1].strip())))

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
    for element in tableau :
        print(element.nom)

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
            indexQuestionsCheveux -= 1
        elif reponseCheveux.upper() == "O" :
            compteurU[0] = 2
        elif reponseCheveux.upper() == "U" :
            compteurU[0] += 1
        if (reponseCheveux.upper() == "O") or (reponseCheveux.upper() == "U"): 
            for personne in tableauIndividus:
                 if personne.couleurDeCheveux == caracteristiquesCheveux[indexQuestionsCheveux]:
                    tableauIndividusEvolutif.add(personne)
        indexQuestionsCheveux += 1
    compteurQuestionsPosees[0] = indexQuestionsCheveux
    return


def questionsYeux():
    indexQuestionsYeux = 0
    listeU = list()
    while compteurU[1] < 2:
        reponseYeux = input(lesQuestionsYeux[indexQuestionsYeux])
        while reponseYeux.upper() not in ["O", "U", "N", "S"]:
            reponseYeux = input(lesQuestionsYeux[indexQuestionsYeux])
        if (reponseYeux.upper() == "S"): 
            suspects(tableauIndividusEvolutif)
            indexQuestionsYeux -= 1
        elif(reponseYeux.upper() == "O"):
            compteurU[1] = 2
            tempSet = set()
            for personne in tableauIndividusEvolutif:
                if personne.couleurDesYeux != caracteristiquesYeux[indexQuestionsYeux]:
                    tempSet.add(personne)
            for personne in tempSet:
                tableauIndividusEvolutif.remove(personne)
            del(tempSet)
        elif reponseYeux.upper() == "U":
            compteurU[1] += 1
            listeU.append(caracteristiquesYeux[indexQuestionsYeux])
        elif reponseYeux.upper() == "N":
            tempSet = set()
            for personne in tableauIndividusEvolutif:
                if personne.couleurDesYeux == caracteristiquesYeux[indexQuestionsYeux]:
                    tempSet.add(personne)
            for personne in tempSet:
                tableauIndividusEvolutif.remove(personne)
            del(tempSet)
        indexQuestionsYeux += 1
    compteurQuestionsPosees[1] = indexQuestionsYeux
    tempSet = set()
    if len(listeU) == 2:
        for personne in tableauIndividusEvolutif:
            if personne.couleurDesYeux != listeU[0] and personne.couleurDesYeux != listeU[1]:
                tempSet.add(personne)
        for personne in tempSet:
            tableauIndividusEvolutif.remove(personne)
        del(tempSet)
    return


def questionsGenie():
    indexQuestionsGenie = 0
    listeU = list()
    while compteurU[2] < 2:
        reponseGenie = input(lesQuestionsGenies[indexQuestionsGenie])
        while reponseGenie.upper() not in ["O", "U", "N", "S"]:
            reponseGenie = input(lesQuestionsGenies[indexQuestionsGenie])
        if reponseGenie.upper() == "S": 
            suspects(tableauIndividusEvolutif)
            indexQuestionsGenie -= 1
        elif reponseGenie.upper() == "O":
            compteurU[2] = 2
            tempSet = set()
            for personne in tableauIndividusEvolutif:
                if personne.genie != caracteristiquesGenie[indexQuestionsGenie]:
                    tempSet.add(personne)
            for personne in tempSet:
                tableauIndividusEvolutif.remove(personne)
            del(tempSet)
        elif reponseGenie.upper() == "U":
            compteurU[2] += 1
        elif reponseGenie.upper() == "N":
            tempSet = set()
            for personne in tableauIndividusEvolutif:
                if personne.genie == caracteristiquesGenie[indexQuestionsGenie]:
                    tempSet.add(personne)
            for personne in tempSet:
                tableauIndividusEvolutif.remove(personne)
            del(tempSet)
        indexQuestionsGenie += 1
    compteurQuestionsPosees[2] = indexQuestionsGenie
    tempSet = set()
    if len(listeU) == 2:
        for personne in tableauIndividusEvolutif:
            if personne.genie != listeU[0] and personne.genie != listeU[1]:
                tempSet.add(personne)
        for personne in tempSet:
            tableauIndividusEvolutif.remove(personne)
        del(tempSet)
    return

tableauIndividusFinale = list()
#  fonction : identifierIndividus()
#   l'agent trouve les noms des deux individues mystères.
def identifierIndividus() : 
    tableauIndividusFiltre = list() 
    questionsCheveux()
    questionsYeux()
    questionsGenie()
    if len(tableauIndividusEvolutif) == 2 : 
        print("Les individues mysteres sont: ", tableauIndividusEvolutif.pop().nom, " et ", tableauIndividusEvolutif.pop().nom)
    elif len(tableauIndividusEvolutif) > 2 : 
        listeIndividus = list()
        for personne in tableauIndividusEvolutif:
            listeIndividus.append(personne)
        index = 0
        personnesTrouvees = False
        compteurU = 0  
        while (not personnesTrouvees and compteurU < 3) :
            if index > len(listeIndividus):
                reponsePersonnes = input("Les personnes suspectes sont-ils " + listeIndividus[index].nom + " et " + listeIndividus[index-1].nom + " ?")
            else:
                reponsePersonnes = input("Les personnes suspectes sont-ils " + listeIndividus[index].nom + " et " + listeIndividus[index+1].nom + " ?")
            while reponsePersonnes.upper() not in ["O", "N", "U", "S"]:
                reponsePersonnes = input("Les personnes suspectes sont-ils " + listeIndividus[index].nom + listeIndividus[index+1].nom)
            if reponsePersonnes.upper() == "S" : 
                suspects(tableauIndividusFiltre)
            elif reponsePersonnes.upper() == "O" : 
                personnesTrouvees = True 
                tableauIndividusFinale.append(listeIndividus[index])
                tableauIndividusFinale.append(listeIndividus[index+1])
                break
            elif reponsePersonnes.upper() == "N":
                compteurU += 1
                if compteurU == 3:
                    break
            elif reponsePersonnes.upper() == "U" :
                compteurU = compteurU + 1 
                tableauIndividusFiltre.append(listeIndividus[index])
                tableauIndividusFiltre.append(listeIndividus[index+1])
                if compteurU == 3:
                    break
            compteurQuestionsPosees[3] = compteurQuestionsPosees[3] + 1 
            index += 2 
            if len(tableauIndividusFiltre) > 2  :
                reponsePersonnesFiltre = input("Les personnes suspectes sont-ils " + tableauIndividusFiltre[0].nom + " et " + tableauIndividusFiltre[2].nom + " ?")
                while reponsePersonnesFiltre.upper() not in ["O", "N", "U", "S"]:
                    reponsePersonnesFiltre = input("Les personnes suspectes sont-ils " + listeIndividus[0].nom  + " et " + listeIndividus[2].nom + " ?")
                if reponsePersonnesFiltre.upper() == "S" : 
                    suspects(tableauIndividusFiltre)
                elif reponsePersonnesFiltre.upper() == "O" :
                    personnesTrouvees = True
                    tableauIndividusFinale.append(tableauIndividusFiltre[0])
                    tableauIndividusFinale.append(tableauIndividusFiltre[2])
                    break
                elif reponsePersonnesFiltre.upper() == "N":
                    compteurU += 1
                    if compteurU == 3:
                        break
                elif reponsePersonnesFiltre.upper() == "U" :
                    compteurU += 1
                    if compteurU == 3:
                        break
                    reponsePersonnesFiltre2 = input("Les personnes suspectes sont-ils " + tableauIndividusFiltre[0].nom + " et " + tableauIndividusFiltre[3].nom + " ?")
                    while reponsePersonnesFiltre2.upper() not in ["O", "N" , "U"]:
                        reponsePersonnesFiltre2 = input("Les personnes suspectes sont-ils " + tableauIndividusFiltre[0].nom + " et " +tableauIndividusFiltre[3].nom + " ?")
                    if reponsePersonnesFiltre2.upper() == "O": 
                        personnesTrouvees = True
                        tableauIndividusFinale.append(tableauIndividusFiltre[0])
                        tableauIndividusFinale.append(tableauIndividusFiltre[3])
                        break
                    elif reponsePersonnesFiltre2.upper() == "U":
                        tableauIndividusFinale.append(tableauIndividusFiltre[0])
                        tableauIndividusFinale.append(tableauIndividusFiltre[3])
                        compteurU += 1
                        if compteurU == 3:
                            break
                    elif reponsePersonnesFiltre2.upper() == "N": 
                        tableauIndividusFinale.append(tableauIndividusFiltre[1])
                        tableauIndividusFinale.append(tableauIndividusFiltre[2])
                        compteurU += 1
                        if compteurU == 3:
                            break
    if (not personnesTrouvees):
        print("Qui sont les personne mysteres? ")
        tableauIndividusFinale.clear()
        tableauIndividusFinale.append(input("Premiere: ")) 
        tableauIndividusFinale.append(input("Deuxieme: "))


#
#  fonction : enleverArcsIndesirables( 3 caracteristiques indesirables )
#   Génère le sous-graphe des caractéristiques désirables.
def get(nom):
    for personnes in tableauIndividus:
        if personnes.nom == nom : 
            return personnes


def enleverArcsIndesirables(cheveux , yeux , genie ) :
    for relations in tableauRelations : 
        if (((get(relations.nomIndividu1)).couleurDeCheveux == (get(relations.nomIndividu2)).couleurDeCheveux) and ((get(relations.nomIndividu1)).couleurDeCheveux == cheveux)) or \
         (((get(relations.nomIndividu1)).couleurDesYeux == (get(relations.nomIndividu2)).couleurDesYeux) and ((get(relations.nomIndividu2)).couleurDesYeux == yeux)) or \
         (((get(relations.nomIndividu1)).genie == (get(relations.nomIndividu2)).genie) and ((get(relations.nomIndividu1)).genie == genie)) :
            if not tableauIndividusFinale.__contains__(get(relations.nomIndividu1)) : 
                relations.facteurRelations = 0 

def lireInputArcs():
    cheveuxIndesirable = input("Nommer la couleur de cheveux indesirables: ")
    while cheveuxIndesirable not in caracteristiquesCheveux:
        cheveuxIndesirable = input("Non-valide. Retaper: ")
    yeuxIndesirable = input("Nommer la couleur des yeux indesirables: ")
    while yeuxIndesirable not in caracteristiquesYeux:
        yeuxIndesirable = input("Non-valide. Retaper: ")
    genieIndesirable = input("Nommer le type de genie indesirables: ")
    while genieIndesirable not in caracteristiquesGenie:
        genieIndesirable = input("Non-valide. Retaper: ")
    return cheveuxIndesirable, yeuxIndesirable, genieIndesirable
#  fonction : trouverChaineContacts( 2 noms d'individus )

#TODO with Dijksta algorithm !!

#   L'agent trouve la meilleure chaine de contacts entre 2 individus à partir 
#   du sous-graphe des caracteristiques désirables.

graphe = collections.defaultdict(dict)
def creerGraphe():
    individu1 = set()
    for relation in tableauRelations:
        individu1.add(relation.nomIndividu1)
    graphe.fromkeys(individu1,0)
    for relation in tableauRelations:
        graphe[relation.nomIndividu1][relation.nomIndividu2] = relation.facteurRelations


def dijkstra(source, cible):
    creerGraphe()
    distanceMinimale = {}
    predecesseur = {}
    relationsNonVisitees = graphe.copy()
    infini = float('inf')
    parcours = []
    for relation in relationsNonVisitees:
        distanceMinimale[relation] = infini
    distanceMinimale[source] = 0

    while relationsNonVisitees:
        relationMinimale = None
        for relation in relationsNonVisitees:
            if relationMinimale is None:
                relationMinimale = relation
            elif distanceMinimale[relation] < distanceMinimale[relationMinimale]:
                relationMinimale = relation

        for relationEnfant, facteurRelations in graphe[relationMinimale].items():
            if facteurRelations + distanceMinimale[relationMinimale] < distanceMinimale[relationEnfant]:
                distanceMinimale[relationEnfant] = facteurRelations + \
                    distanceMinimale[relationMinimale]
                predecesseur[relationEnfant] = relationMinimale
        relationsNonVisitees.pop(relationMinimale)

    currentrelation = cible
    while currentrelation != source:
        try:
            parcours.insert(0, currentrelation)
            currentrelation = predecesseur[currentrelation]
        except KeyError:
            print('parcours impossible a etablir')
            break
    parcours.insert(0, source)
    if distanceMinimale[cible] != infini:
        print('distance minimale est ' + str(distanceMinimale[cible]))
        print('Le parcours est ' + str(parcours))


def trouverChaineContacts(nomSource, nomCible):
    dijkstra(nomSource, nomCible)
#  fontion : afficherResultat() 
#   L'agent présente le résultatde ses accomplissements selon le bon format.
def afficherResultat(c,y,g) :
    for relation in tableauRelations:
        if relation.facteurRelations != 0:
            print("(%s,%s(%s%%))\n" % (relation.nomIndividu1.strip(), relation.nomIndividu2.strip(), str(relation.facteurRelations).strip()))
    if len(tableauIndividusFinale) == 2: 
        trouverChaineContacts(tableauIndividusFinale[0], tableauIndividusFinale[1])
    nombreQuestions = compteurQuestionsPosees[0] + compteurQuestionsPosees[1] + compteurQuestionsPosees[2] + compteurQuestionsPosees[3]
    print("Nombre de questions posees: ", nombreQuestions ,"\n")
    if len(tableauIndividusFinale) == 2: 
        print("Les individus mysteres sont ", tableauIndividusFinale[0], tableauIndividusFinale[1])
    print()
    print("Caracteristiques indesirables: ",c,y,g)
        
    return
# Interface console qui affiche le menu : 
#   a/ Créer le résea social.
#   b/ Afficher le réseau social.
#   c/ Jouer à Qui est-ce ? 
#   d/ Afficher le résultat.
#   e/ Quitter. 
#
########################

def lireInputMenu() :
    valeur = input()
    if valeur.lower() not in ["a","b","c","d","e"]:
        print("Index Invalide, reessayez:\n")
        valeur = "m"
    return valeur.lower()

# main 
def main() :
    current = "m"
    c = None
    y = None
    g = None
    #Menu
    while True:
        if current == "m":
            print("a/ Créer le réseau social.")
            print("b/ Afficher le réseau social.")
            print("c/ Jouer à Qui est-ce ?")
            print("d/ Afficher le résultat.")
            print("e/ Quitter")
            current = lireInputMenu()
        elif current == "a":
            file1 = input("Fichier Individus(avec extension): ")
            file2 = input("Fichier Relations(avec extension): ")
            creerReseauSocial(file1, file2)
            current = "m"
        elif current == "b": 
            afficherReseauSocial()
            current = "m"
        elif current == "c":#Verifier que ca fontionne
            identifierIndividus()
            c, y, g = lireInputArcs()
            enleverArcsIndesirables(c, y, g)
            current = "m"
        elif current == "d":
            afficherResultat(c,y,g)
            current = "m"
        elif current == "e":
            break

if __name__== "__main__":
    main()
