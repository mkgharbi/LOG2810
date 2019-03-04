import collections

#Classe :

class Personne:
    def __init__(self, nom, couleurDeCheveux, couleurDesYeux, genie):
        self.__nom = nom
        self.__couleurDeCheveux = couleurDeCheveux
        self.__couleurDesYeux = couleurDesYeux
        self.__genie = genie

    def getNom(self):
        return self.__nom

    def getCouleurDeCheveux(self):
        return self.__couleurDeCheveux

    def getCouleurDesYeux(self):
        return self.__couleurDesYeux

    def getGenie(self):
        return self.__genie

    def setNom(self, nom):
        self.__nom = nom

    def setCouleurDeCheveux(self, couleurDeCheveux):
        self.__couleurDeCheveux = couleurDeCheveux

    def setCouleurDesYeux(self, couleurDesYeux):
        self.__couleurDesYeux = couleurDesYeux

    def setGenie(self, genie):
        self.__genie = genie


class Relations:
    def __init__(self, individu1, individu2, facteurRelations):
        self.__individu1 = individu1
        self.__individu2 = individu2
        self.__facteurRelations = facteurRelations

    def getIndividu1(self):
        return self.__individu1

    def getIndividu2(self):
        return self.__individu2

    def getFacteurRelations(self):
        return self.__facteurRelations

    # est ce le paramettre va se melanger avec celui du par constructeur
    def setIndividu1(self, individu1):
        self.__individu1 = individu1

    def setindividu2(self, individu2):
        self.__individu2 = individu2

    def setFacteurRelations(self, facteurRelations):
        self.__facteurRelations = facteurRelations

tableauRelations = set() #Ce tableau contient tout les relations et deviendrat eventuellement le sous-graphe des caracteres indesirables
tableauIndividus = set() #Ce tableau contient tout les individus

#  fonction : trouverPersonne( ) :
#   Retourne une personne a partir du nom
def trouverPersonne(nom):
    for personne in tableauIndividus:
        if personne.getNom() == nom:
            return personne

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
        if int(chaines[1].strip()) > 0 and int(chaines[1].strip()) <= 100:
            tableauRelations.add(Relations(chaines[0].strip(), chaines[2].strip(), int(chaines[1].strip())))

#  fonction : afficherReseauSocial()
#   Affiche le réseau social selon le format présenté en annexe.
def afficherReseauSocial():
    #creerReseauSocial("individus.txt","Relations.txt")
    if len(tableauRelations) == 0:
        print("Aucun Reseau Trouver!\n")
        return
    for relation in tableauRelations:
        print("(%s,%s(%s%%))\n" % (relation.getIndividu1().strip(), relation.getIndividu2().strip(), str(relation.getFacteurRelations()).strip()))

# Conteneurs des caracteristiques et des questions
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

caracteristiquesGenie = ["GI", "GP", "GE","GC", "GA", "GM", "GB", "GInd", "ER"]

lesQuestionsGenies = [" Les individus sont-ils en génie informatique-GI ?",
                        " Les individus sont-ils en génie physique-GP ?",
                        " Les individus sont-ils en génie electrique-GE ?",
                        " Les individus sont-ils en génie chimique-GC ?",
                        " Les individus sont-ils en génie aerospatial-GA ?",
                        " Les individus sont-ils en génie mecanique-GM ?",
                        " Les individus sont-ils en génie biomédical-GB ?",
                        " Les individus sont-ils en génie industriel-GInd ?",
                        " Les individus sont-ils en génie énergétique-ER ?"]

compteurQuestionsPosees = [0, 0, 0, 0] #Contient le nombre de questions posees au total
compteurU = [0, 0, 0] #Contient le nombre de questions posees pour une caracterisitque et sera utiliser afin de s'assurer qu'on ne pose pas trop de questions
tableauIndividusEvolutif = set() #Le tableau qui contiendra d'abord les personnes ayant les cheveux voulus, et ensuite elimine eux avec les yeux et genie non-voulus

# fonction : suspects()
# Affiche la liste des suspects
def suspects(tableau):
    print("Les suspects sont :")
    for personne in tableau:
        print(personne.getNom())

# fonction : questionsCheveux()
# Pose les questions sur les cheveux et interprete les reponses
def questionsCheveux():
    indexQuestionsCheveux = 0
    while compteurU[0] < 2:
        reponseCheveux = input(lesQuestionsCheveux[indexQuestionsCheveux])
        while reponseCheveux.upper() not in ["O", "N", "U", "S"]:
            reponseCheveux = input(lesQuestionsCheveux[indexQuestionsCheveux])
        if reponseCheveux.upper() == "S":
            suspects(tableauIndividusEvolutif)
            indexQuestionsCheveux -= 1
        elif reponseCheveux.upper() == "O":
            compteurU[0] = 2
        elif reponseCheveux.upper() == "U":
            compteurU[0] += 1
        if (reponseCheveux.upper() == "O") or (reponseCheveux.upper() == "U"):
            for personne in tableauIndividus:
                if personne.getCouleurDeCheveux() == caracteristiquesCheveux[indexQuestionsCheveux]:
                    tableauIndividusEvolutif.add(personne)
        indexQuestionsCheveux += 1
    compteurQuestionsPosees[0] = indexQuestionsCheveux
    return

# fonction : questionsYeux()
# Pose les questions sur les yeux et interprete les reponses
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
                if personne.getCouleurDesYeux() != caracteristiquesYeux[indexQuestionsYeux]:
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
                if personne.getCouleurDesYeux() == caracteristiquesYeux[indexQuestionsYeux]:
                    tempSet.add(personne)
            for personne in tempSet:
                tableauIndividusEvolutif.remove(personne)
            del(tempSet)
        indexQuestionsYeux += 1
    compteurQuestionsPosees[1] = indexQuestionsYeux
    tempSet = set()
    if len(listeU) == 2:
        for personne in tableauIndividusEvolutif:
            if personne.getCouleurDesYeux() != listeU[0] and personne.getCouleurDesYeux() != listeU[1]:
                tempSet.add(personne)
        for personne in tempSet:
            tableauIndividusEvolutif.remove(personne)
        del(tempSet)
    return

# fonction : questionsGenie()
# Pose les questions sur les yeux et interprete les reponses
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
                if personne.getGenie() != caracteristiquesGenie[indexQuestionsGenie]:
                    tempSet.add(personne)
            for personne in tempSet:
                tableauIndividusEvolutif.remove(personne)
            del(tempSet)
        elif reponseGenie.upper() == "U":
            compteurU[2] += 1
        elif reponseGenie.upper() == "N":
            tempSet = set()
            for personne in tableauIndividusEvolutif:
                if personne.getGenie() == caracteristiquesGenie[indexQuestionsGenie]:
                    tempSet.add(personne)
            for personne in tempSet:
                tableauIndividusEvolutif.remove(personne)
            del(tempSet)
        indexQuestionsGenie += 1
    compteurQuestionsPosees[2] = indexQuestionsGenie
    tempSet = set()
    if len(listeU) == 2:
        for personne in tableauIndividusEvolutif:
            if personne.getGenie() != listeU[0] and personne.getGenie() != listeU[1]:
                tempSet.add(personne)
        for personne in tempSet:
            tableauIndividusEvolutif.remove(personne)
        del(tempSet)
    return


tableauIndividusFinale = list() #Ce tableau contient les personnes mysteres finales
tableauPersonnesMysteresIntrouvees = list() #Ce tableau contient les personnes mysteres qui n'ont pas ete identifier par le tableau de tentatives
tableauTentative = list() #Ce tableau contient les tentatives et s'assure de memoriser les U qui sont valides
tableauPersonnesMysteresTrouvees = list() #Ce tableau contient les personnes mysteres qui ont ete identifier par le tableau de tentatives
personneMystere1 = "" #Utiliser a titre de comparaison avec le tableau de tentative
personneMystere2 = "" #Meme chose

def containsByName(nom,tableau): 
    counter = 0  
    while ( counter != len(tableau) ): 
        if tableau[counter] == nom : 
            return True 
        counter += 1 
    return False

#  fonction : identifierIndividus()
#  Tente de trouver les noms des deux individues mystères. On repete la sequence trois foit afin de permettre la memorisation par le tableau de #  tentative
def identifierIndividus():
    tableauIndividusFiltre = list()
    personnesTrouvees = False
    questionsCheveux()
    questionsYeux()
    questionsGenie()
    if len(tableauIndividusEvolutif) == 2:
        print("Les individues mysteres sont: ", tableauIndividusEvolutif.pop().getNom(), " et ", tableauIndividusEvolutif.pop().getNom())
    elif len(tableauIndividusEvolutif) > 2:
        listeIndividus = list()
        for personne in tableauIndividusEvolutif:
            listeIndividus.append(personne)
        index = 0
        compteurU = 0
        while (not personnesTrouvees and compteurU < 3):
            if index+1 >= len(listeIndividus):
                index -= 1
                reponsePersonnes = input("Les personnes suspectes sont-ils " + listeIndividus[index].getNom() + " et " + listeIndividus[index+1].getNom() + " ?")
            else:
                reponsePersonnes = input("Les personnes suspectes sont-ils " + listeIndividus[index].getNom() + " et " + listeIndividus[index+1].getNom() + " ?")
            while reponsePersonnes.upper() not in ["O", "N", "U", "S"]:
                if index+1 >= len(listeIndividus):
                    index -= 1
                reponsePersonnes = input("Les personnes suspectes sont-ils " + listeIndividus[index].getNom() + listeIndividus[index+1].getNom())
            tableauTentative.append(listeIndividus[index].getNom())
            tableauTentative.append(listeIndividus[index+1].getNom())
            if reponsePersonnes.upper() == "S":
                suspects(listeIndividus)
                index -= 2
            elif reponsePersonnes.upper() == "O":
                
                personnesTrouvees = True
                tableauPersonnesMysteresTrouvees.append(listeIndividus[index].getNom())
                tableauPersonnesMysteresTrouvees.append(listeIndividus[index+1].getNom())
                break
            elif reponsePersonnes.upper() == "N":
                tableauTentative.clear()
                compteurU += 1
                if compteurU == 3:
                    break
            elif reponsePersonnes.upper() == "U":
                compteurU = compteurU + 1
                tableauIndividusFiltre.append(listeIndividus[index].getNom())
                tableauIndividusFiltre.append(listeIndividus[index+1].getNom())
                if (compteurU < 3 ) : 
                    tableauTentative.clear()
                if compteurU == 3:
                    break
            compteurQuestionsPosees[3] = compteurQuestionsPosees[3] + 1
            index += 2
            if len(tableauIndividusFiltre) > 2:
                reponsePersonnesFiltre = input("Les personnes suspectes sont-ils " + tableauIndividusFiltre[0] + " et " + tableauIndividusFiltre[2] + " ?")
                while reponsePersonnesFiltre.upper() not in ["O", "N", "U", "S"]:
                    reponsePersonnesFiltre = input("Les personnes suspectes sont-ils " + tableauIndividusFiltre[0] + " et " + tableauIndividusFiltre[2] + " ?")
                tableauTentative.append(listeIndividus[index].getNom())
                tableauTentative.append(listeIndividus[index+1].getNom())
                if reponsePersonnesFiltre.upper() == "S":
                    suspects(tableauIndividusFiltre)

                elif reponsePersonnesFiltre.upper() == "O":
                    personnesTrouvees = True
                    tableauPersonnesMysteresTrouvees.append(tableauIndividusFiltre[0])
                    tableauPersonnesMysteresTrouvees.append(tableauIndividusFiltre[2])
                    break
                elif reponsePersonnesFiltre.upper() == "N":
                    tableauTentative.clear()
                    compteurU += 1
                    if compteurU == 3:
                        break
                elif reponsePersonnesFiltre.upper() == "U":
                    tableauIndividusFiltre.append(listeIndividus[index].getNom())
                    tableauIndividusFiltre.append(listeIndividus[index+1].getNom())
                    if (compteurU < 2 ) : 
                        tableauTentative.clear()
                    compteurU += 1
                    if compteurU == 3:
                        break
                    reponsePersonnesFiltre2 = input("Les personnes suspectes sont-ils " + tableauIndividusFiltre[0] + " et " + tableauIndividusFiltre[3] + " ?")
                    while reponsePersonnesFiltre2.upper() not in ["O", "N", "U"]:
                        reponsePersonnesFiltre2 = input("Les personnes suspectes sont-ils " + tableauIndividusFiltre[0] + " et " + tableauIndividusFiltre[3] + " ?")
                    tableauTentative.append(listeIndividus[index].getNom())
                    tableauTentative.append(listeIndividus[index+1].getNom())
                    if reponsePersonnesFiltre2.upper() == "O":
                        personnesTrouvees = True
                        tableauPersonnesMysteresTrouvees.append(tableauIndividusFiltre[0])
                        tableauPersonnesMysteresTrouvees.append(tableauIndividusFiltre[3])
                        break
                    elif reponsePersonnesFiltre2.upper() == "U":
                        tableauPersonnesMysteresTrouvees.append(tableauIndividusFiltre[0])
                        tableauPersonnesMysteresTrouvees.append(tableauIndividusFiltre[3])
                        compteurU += 1
                        if compteurU < 1 :
                            tableauTentative.clear()
                        if compteurU == 3:
                            break
                    elif reponsePersonnesFiltre2.upper() == "N":
                        tableauTentative.clear()
                        tableauPersonnesMysteresTrouvees.append(tableauIndividusFiltre[1])
                        tableauPersonnesMysteresTrouvees.append(tableauIndividusFiltre[2])
                        compteurU += 1
                        if compteurU == 3:
                            break
    if (not personnesTrouvees): #En d'autres termes, jamais dit "oui"
        print("Qui sont les personne mysteres? ")
        tableauIndividusFinale.append(input("Premiere: "))
        personneMystere1 = tableauIndividusFinale[0]
        tableauIndividusFinale.append(input("Deuxieme: "))
        personneMystere2 = tableauIndividusFinale[1]

        if personneMystere1 not in tableauTentative :
            tableauPersonnesMysteresIntrouvees.append(personneMystere1)
        elif personneMystere1 in tableauTentative :
            if len(tableauPersonnesMysteresTrouvees) < 1:
                tableauPersonnesMysteresTrouvees.append(personneMystere1)
            else:
                tableauPersonnesMysteresTrouvees[0] = personneMystere1

        if personneMystere2 not in tableauTentative :
            tableauPersonnesMysteresIntrouvees.append(personneMystere2)
        elif personneMystere2 in tableauTentative :
            if len(tableauPersonnesMysteresTrouvees) < 2:
                tableauPersonnesMysteresTrouvees.append(personneMystere1)
            else:
                tableauPersonnesMysteresTrouvees[1] = personneMystere1
    else:
        tableauIndividusFinale.append(tableauPersonnesMysteresTrouvees[0])
        tableauIndividusFinale.append(tableauPersonnesMysteresTrouvees[1])

# fonction : getPersonne()
# Utilise le nom passer en parametre pour retourner la personne
tableauMysteree = [personneMystere1 , personneMystere2] #tableau temporaire pour contenir les valeurs du tableau finale
def getPersonne(nom) : 
    for personne in tableauIndividus: 
        if personne.getNom() == nom : 
            return personne

#  fonction : enleverArcsIndesirables( 3 caracteristiques indesirables )
#  Génère le sous-graphe des caractéristiques désirables.
def enleverArcsIndesirables(cheveux, yeux, genie):
    for relations in tableauRelations:
        if ((getPersonne(relations.getIndividu1()).getCouleurDeCheveux() == getPersonne(relations.getIndividu2()).getCouleurDeCheveux()) and ((getPersonne(relations.getIndividu1()).getCouleurDeCheveux() == cheveux))) or \
            ((getPersonne(relations.getIndividu1()).getCouleurDesYeux() == getPersonne(relations.getIndividu2()).getCouleurDesYeux()) and (getPersonne(relations.getIndividu2()).getCouleurDesYeux() == yeux)) or \
                ((getPersonne(relations.getIndividu1()).getGenie() == getPersonne(relations.getIndividu2()).getGenie()) and (getPersonne(relations.getIndividu1()).getGenie == genie)):
            if not (tableauMysteree.__contains__(relations.getIndividu1()) or tableauMysteree.__contains__(relations.getIndividu2())):
                relations.setFacteurRelations(0)

# fonction : lireInputArcs()
# Lit et retourne l'input de l'utilisateur a propos des caracteristiques indesirables
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

# fonction : creerGraphe()
# Cree le graphe contenant les relations bidirectionelles entre individus
graphe = collections.defaultdict(dict) #Dictionaire bidirectionel afin de simuler un graphe
def creerGraphe():
    individu1 = set()
    for individu in tableauIndividus:
        individu1.add(individu.getNom())
    graphe.fromkeys(individu1,0)
    for relation in tableauRelations:
<<<<<<< HEAD
        graphe[relation.getIndividu1()][relation.getIndividu2()] = relation.getFacteurRelations()
        graphe[relation.getIndividu2()][relation.getIndividu1()] = relation.getFacteurRelations()
=======
        if relation.getFacteurRelations() != 0:
            graphe[relation.getIndividu1().getNom()][relation.getIndividu2().getNom()] = relation.getFacteurRelations()
>>>>>>> 40094c8fcb785da09fec2d226a9fb71b38233359

#  fonction : trouverChaineContacts( 2 noms d'individus )
#   L'agent trouve la meilleure chaine de contacts entre 2 individus à partir
#   du sous-graphe des caracteristiques désirables avec l'algorithme de Dijskstra
def trouverChaineContacts(source, cible):
    creerGraphe()
    distanceMinimale = {}
    predecesseur = {}
    relationsNonVisitees = graphe.copy()
    infini = 999999
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
                distanceMinimale[relationEnfant] = facteurRelations + distanceMinimale[relationMinimale]
                predecesseur[relationEnfant] = relationMinimale
        relationsNonVisitees.pop(relationMinimale)

    currentrelation = cible
    while currentrelation != source:
        try:
            parcours.insert(0, currentrelation)
            currentrelation = predecesseur[currentrelation]
        except KeyError:
            print("parcours non-valide")
            break
    parcours.insert(0, source)
    if distanceMinimale[cible] != infini:
        print('Le parcours est ' + str(parcours))

#  fontion : afficherResultat()
#   L'agent présente le résultatde ses accomplissements selon le bon format.
def afficherResultat(c, y, g):
    for relation in tableauRelations:
        if relation.getFacteurRelations() != 0:
            print("(%s,%s(%s%%))\n" % (relation.getIndividu1().strip(), relation.getIndividu2().strip(), str(relation.getFacteurRelations()).strip()))
    trouverChaineContacts(tableauIndividusFinale[0], tableauIndividusFinale[1])
    nombreQuestions = compteurQuestionsPosees[0] + compteurQuestionsPosees[1] + compteurQuestionsPosees[2] + compteurQuestionsPosees[3]
    print("Nombre de questions posees: ", nombreQuestions+1, "\n")
    if len(tableauPersonnesMysteresTrouvees) == 0 :
        print("L'agent n'a pas trouve les personnes mysteres.")
    else :
        print("Les personnes mysteres trouvees sont : ")
        for element in tableauPersonnesMysteresTrouvees : 
            print(element)
    if len(tableauPersonnesMysteresIntrouvees) == 0 : 
        print("L'agent a trouve les 2 personnes mysteres")
    else : 
        print("Les personnes mysteres non-trouvees sont : ")
        for element in tableauPersonnesMysteresIntrouvees: 
            print(element)
    print("Caracteristiques indesirables: ", c, y, g)
    return

# fonction : lireInputMenu()
# Lit et retourne l'input de l'utilisateur pour le Menu Principale
def lireInputMenu():
    valeur = input()
    if valeur.lower() not in ["a", "b", "c", "d", "e"]:
        print("Index Invalide, reessayez:\n")
        valeur = "m"
    return valeur.lower()

# fonction : main()
#  1)S'occupe du deroulement du programme
#  2)Interface console qui affiche le menu :
#   a/ Créer le résea social.
#   b/ Afficher le réseau social.
#   c/ Jouer à Qui est-ce ?
#   d/ Afficher le résultat.
#   e/ Quitter.
#
########################
def main():
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
        elif current == "c": 
            identifierIndividus()
            c, y, g = lireInputArcs()
            enleverArcsIndesirables(c, y, g)
            current = "m"
        elif current == "d":
            afficherResultat(c, y, g)
            current = "m"
        elif current == "e":
            break

#Permet la simulation d'un main
if __name__ == "__main__":
    main()
