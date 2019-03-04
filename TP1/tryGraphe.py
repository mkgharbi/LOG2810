
from collections import defaultdict, deque


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)


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
            tableauRelations.add(
                Relations(Personne1, Personne2, int(chaines[1].strip())))


#graphe = collections.defaultdict(dict)


#def creerGraphe():
#    individu1 = set()
#    for relation in tableauRelations:
#        individu1.add(relation.getIndividu1())
#    graphe.fromkeys(individu1, 0)
#    for relation in tableauRelations:
#        graphe[relation.getIndividu1().getNom()][relation.getIndividu2().getNom()] = relation.getFacteurRelations()




def main() :

    creerReseauSocial("Individus.txt", "Relations.txt")

    graph = Graph()

    personneIndiv1 = set()
    for relation in tableauRelations: 
        personneIndiv1.add(relation.getIndividu1())
    
    for personne in personneIndiv1: 
        graph.add_node(personne)

    for relations in tableauRelations: 
        graph.add_edge(relations.getIndividu1(),relations.getIndividu2(),relations.getFacteurRelations())

    print(graph)

    print(shortest_path(graph, personneMystere1,personneMystere2))
    
    #creerGraphe()

if __name__== "__main__":
    main()
