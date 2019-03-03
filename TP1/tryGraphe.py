
import collections

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


graphe = collections.defaultdict(dict)
def creerGraphe():
    individu1 = set()
    for individu in tableauIndividus:
        individu1.add(individu.nom)
    graphe.fromkeys(individu1,0)
    for relation in tableauRelations:
        graphe[relation.nomIndividu1][relation.nomIndividu2] = relation.facteurRelations
        graphe[relation.nomIndividu2][relation.nomIndividu1] = relation.facteurRelations



def main() : 
    creerReseauSocial("Individus.txt","Relations.txt")
    creerGraphe()
    print(graphe)

if __name__== "__main__":
    main()