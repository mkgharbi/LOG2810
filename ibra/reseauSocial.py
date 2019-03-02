########################


#Classe :
class Personne:

    def _init_(self, nom, couleurDeCheveux, couleurDesYeux, genie):
        self.nom = nom
        self.couleurDeCheveux = couleurDeCheveux
        self.couleurDesYeux = couleurDesYeux
        self.genie = genie
    def __str__(self):
        return 



class Relations: 
    def _init_ (self, nomIndividu1 , nomIndividu2, facteurRelations):
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
    for ind in individus:
        personne = ind.split(" ")
        tableauIndividus.add(Personne(personne[0], personne[1], personne[2], personne[3]))
    for lignes in relations:  
        chaines = lignes.split(" ")
        if chaines[1] > 0 and chaines[1] <= 100:
            tableauRelations.add(Relations(chaines[0], chaines[2], chaines[1]))


#
#  fonction : afficherReseauSocial()
#   Affiche le réseau social selon le format présenté en annexe.
def afficherReseauSocial():
    #creerReseauSocial("individus.txt","Relations.txt")
    for x in tableauRelations:
        print(x.nomIndividu1 , " , " , x.nomIndividu2 , " ( " , x.facteurRelations , " % )")


