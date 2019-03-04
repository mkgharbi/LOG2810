
import collections

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

tableauRelations = set()
tableauIndividus = set()

def trouverPersonne(nom):
    for personne in tableauIndividus:
        if personne.getNom() == nom:
            return personne

def creerReseauSocial(fichier1, fichier2):
    individus = open(fichier1, "r")
    relations = open(fichier2, "r")
    for ligne in individus:
        personne = ligne.split(" ")
        tableauIndividus.add(Personne(personne[0].strip(), personne[1].strip(), personne[2].strip(), personne[3].strip()))
    for ligne in relations:  
        chaines = ligne.split(" ")
        if int(chaines[1]) > 0 and int(chaines[1]) <= 100:
            Personne1 = trouverPersonne(chaines[0].strip())
            Personne2 = trouverPersonne(chaines[2].strip())
            tableauRelations.add(Relations(Personne1, Personne2, int(chaines[1].strip())))



graphe = collections.defaultdict(dict)
def creerGraphe():
    individu1 = set()
    for individu in tableauIndividus:
        individu1.add(individu.getNom())
    graphe.fromkeys(individu1,0)
    for relation in tableauRelations:
        graphe[relation.getIndividu1().getNom()][relation.getIndividu2().getNom()] = relation.getFacteurRelations()
        graphe[relation.getIndividu2().getNom()][relation.getIndividu1().getNom()] = relation.getFacteurRelations()



def main() : 
    creerReseauSocial("Individus.txt","Relations.txt")
    creerGraphe()
    print(graphe)

if __name__== "__main__":
    main()