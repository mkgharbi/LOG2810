import heapq
import collections

class HeapEntry:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key, neighbours):
        self.nodes[key] = neighbours

    def traceback_path(self, target, parents):
        path = []
        while target:
            path.append(target)
            target = parents[target]
        return list(reversed(path))

    def shortest_path(self, start, finish):
        OPEN = [HeapEntry(start, 0.0)]
        CLOSED = set()
        parents = {start: None}
        distance = {start: 0.0}

        while OPEN:
            current = heapq.heappop(OPEN).node

            if current is finish:
                return self.traceback_path(finish, parents)

            if current in CLOSED:
                continue

            CLOSED.add(current)

            for child in self.nodes[current].keys():
                if child in CLOSED:
                    continue
                tentative_cost = distance[current] + self.nodes[current][child]

                if child not in distance.keys() or distance[child] > tentative_cost:
                    distance[child] = tentative_cost
                    parents[child] = current
                    heap_entry = HeapEntry(child, tentative_cost)
                    heapq.heappush(OPEN, heap_entry)





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

    def setIndividu1(self, individu1):
        self.__individu1 = individu1

    def setindividu2(self, individu2):
        self.__individu2 = individu2

    def setFacteurRelations(self, facteurRelations):
        self.__facteurRelations = facteurRelations



def trouverPersonne(nom):
    for personne in tableauIndividus:
        if personne.getNom() == nom:
            return personne



tableauRelations = set()
tableauIndividus = set()


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


graphe = Graph()
dictionnaire = collections.defaultdict(dict)


def creerGraphe():
    individu1 =  set()
    for individu in tableauRelations:
        individu1.add(individu.getIndividu1().getNom())
    dictionnaire.fromkeys(individu1)
    for personne in individu1 :
        for relation in tableauRelations:
            if personne == relation.getIndividu1().getNom() : 
                if relation.getFacteurRelations() != 0:
                    dictionnaire[relation.getIndividu1().getNom()][relation.getIndividu2().getNom()] = relation.getFacteurRelations()
        graphe.add_node(personne,dictionnaire[personne])



def main(): 
<<<<<<< HEAD
    creerReseauSocial("Individus.txt","Relations.txt")
=======
    creerReseauSocial("Inidividus.txt","Relations.txt")
>>>>>>> 40094c8fcb785da09fec2d226a9fb71b38233359
    creerGraphe()
    print(graphe)

    print(graphe.shortest_path("Maximer", "Adam"))

<<<<<<< HEAD
if __name__ == "__main__":
    main()
=======

>>>>>>> 40094c8fcb785da09fec2d226a9fb71b38233359
