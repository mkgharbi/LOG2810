
########################


#Classe : 
class Personne :
    
    def _init_(self, nom, couleurDeCheveux, couleurDesYeux, genie) :
        self.nom = nom
        self.couleurDeCheveux = couleurDeCheveux
        self.couleurDesYeux = couleurDesYeux
        self.genie = genie

tableauRelations =  [] 

#TODO : 

#  fontion : creerReseauSocial( , ) : 
#   Lire les fichiers texte contenant les informations 
#   et genere le reseau social correspondant. 
def creerReseauSocial(fichier1 , fichier2) : 
    individus = open(fichier1,"r")
    relations = open(fichier2 , "r")
    for i in relations : 
        relations[i].split(" ")
        if relations[1] > 0 and relations[1] <=100 :
            tableaRelations.append(" ( " + relations[0] + "  " + relations[2] + "  ( " + relations[1] + "%") 
            

#
#  fonction : afficherReseauSocial() 
#   Affiche le réseau social selon le format présenté en annexe. 
def afficherReseauSocial() :
    for x in array : 
        print()
# 
#  fonction : identifierIndividus()
#   l'agent trouve les noms des deux individues mystères.
def identifierIndividus() : 

#
#  fonction : enleverArcsIndesirables( 3 caracteristiques indesirables )
#   Génère le sous-graphe des caractéristiques désirables.
def enleverArcsIndesirables() : 

#  fonction : trouverChaineContacts( 2 noms d'individus )
#   L'agent trouve la meilleure chaine de contacts entre 2 individus à partir 
#   du sous-graphe des caracteristiques désirables.

def trouverChaineContacts() :  

#  fontion : afficherResultat() 
#   L'agent présente le résultatde ses accomplissements selon le bon format.
def afficherResultat() :

# Interface console qui affiche le menu : 
#   a/ Créer le résea social.
#   b/ Afficher le réseau social.
#   c/ Jouer à Qui est-ce ? 
#   d/ Afficher le résultat.
#   e/ Quitter. 
#
########################


# main 
def main() : 
    
