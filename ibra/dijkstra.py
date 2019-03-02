from Suspect import *
from reseauSocial import *
# relation c'est pour lire le tableau de relation 
# premSuspect est la premier personne qu'on pense avoir trouver sert pour lire comme au debut de le tableau de relation
#deuxSuspect est le deuxieme personne qu'on doit trouver la fin de notre lecture 
def shortPath(Relations,premSuspect, deuxSuspect) :
    #on fait un tableau ou la colonne 0 reprensente nom des individu 
    #1 eme colonne antecedant est ce qu'il a ete parcouru
    #2 eme colonne on met le poid de l'arret
    #3 eme colonne 
