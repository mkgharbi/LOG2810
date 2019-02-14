
########################


#Classe : 
class Personne :
    
    def _init_(self, nom, couleurDeCheveux, couleurDesYeux, genie) :
        self.nom = nom
        self.couleurDeCheveux = couleurDeCheveux
        self.couleurDesYeux = couleurDesYeux
        self.genie = genie

tableauRelations =  [] 
tableauIndividus = [] 


#TODO : 

#  fontion : creerReseauSocial( , ) : 
#   Lire les fichiers texte contenant les informations 
#   et genere le reseau social correspondant. 
def creerReseauSocial(fichier1 , fichier2) : 
    individus = open(fichier1,"r")
    relations = open(fichier2 , "r")
    for ind in individus : 
        personne = ind.split(" ")
        tableauIndividus.append(Personne(personne[0], personne[1], personne[2] ,personne[3] ))
    for lignes in relations :  # A verifier 
        chaines = lignes.split(" ")
        if chaines[1] > 0 and chaines[1] <=100 :
            tableauRelations.append(" ( " + chaines[0] + "  " + chaines[2] + "  ( " + chaines[1] + "%") 
            

#
#  fonction : afficherReseauSocial() 
#   Affiche le réseau social selon le format présenté en annexe. 
def afficherReseauSocial() :
    for x in tableauRelations : 
        print(tableauRelations[x])
# 


questionsCheveux = ["Les individues mysteres ont-ils les cheveux noirs-N ? ",
                    "Les individues mysteres ont-ils les cheveux roux-R ? " , 
                    "Les individues mysteres ont-ils les cheveux blonds-B ? " , 
                    "Les individues mysteres ont-ils les cheveux marrons-M ? " ]

questionsYeux = [   "Les individues mysteres ont-ils les yeux bleus-B ? " , 
                    "Les individues mysteres ont-ils les yeux verts-V ? " , 
                    "Les individues mysteres ont-ils les yeux noirs-N ? " ,
                    "Les individues mysteres ont-ils les yeux gris-G ? " , 
                    "Les individues mysteres ont-ils les yeux marrons-M ? ",  ]

questionsGenies = [ " Les individus sont-ils en génie informatique-GI ?"
                    " Les individus sont-ils en génie physique-GP ?"
                    " Les individus sont-ils en génie electrique-GE ?"
                    " Les individus sont-ils en génie chimique-GC ?"
                    " Les individus sont-ils en génie aerospatial-GA ?"
                    " Les individus sont-ils en génie mecanique-GM ?"
                    " Les individus sont-ils en génie biomédical-GB ?"
                    " Les individus sont-ils en génie industriel-GInd ?"
                    " Les individus sont-ils en génie énergétique-ER ?"]

compteurQuestionsPosees = [0 , 0 , 0 ]

# Decoupage de la fonction identifierIndividus() : 
# Questions a poser (compteur locale)
def questions
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
    #1. adversaire 
