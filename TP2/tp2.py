terminaux = ["","a", "b", "c", "d", "e"]
nonTerminaux = ["A","B", "C", "D",  "S"]

#facile 
tableauFichier =[]#tableau des fichier données 
def remplirFichier (nbrFichier):
    t = True
    #remplir le tableau avec les fichier 
    #on devera faire une boucle ou on met les 21 fichier c'est long d'ecrire 21 fichier 

#ef lireFichier():#lire les fichier
    #cette fonction dois:lire les fichier (utiliser la fonction lireFichier),
    #crée l'automate , valider le mot de passe, retourne une liste de portes
#compliquer

States = []
inputs = [] 
nextState = [] 

def ouvrirPorte (fichier, numero): 
    porte = open (fichier, "r")
    porte.next()
    tempGrammar = porte.read()
    arrayGrammar = tempGrammar.split(", ")
    genererAutomate(arrayGrammar, porte, numero)  # call genererAutomate
    

#moyen
def affronterLeBoss():
    t = True
    #lis le fichier Boss.txt
    #generer l'automate associé au chemin decrit dans le fichier 
    #valider la concatenation des mot de passe des le debut 
    #trouver le language

#moyen
def getMax(array):
    maximum = array[0].length()
    for item in array: 
        if maximum < item.length() : 
            maximum = item.length()
    return maximum 



def genererCode(array,max):
    returnArray = []
    return returnArray



def genererAutomate (array, file, numero):
    file.next()
    tempArray = []
    while True:
        currentLine = file.read()
        if currentLine is None:
            break
        currentLineArray = currentLine.split(" ")
        tempArray.append(currentLineArray[0], currentLineArray[1])
    porteArray = []
    passwordArray = []
    for current in tempArray:
        if "Porte" in current:
            porteArray.append(current)
        else:
            passwordArray.append(current)
    tempArray.clear()
    codeArray = genererCode(array, getMax(passwordArray))
    codeArray.append("")




#facile
def afficherLeCheminParcouru():
    t = True
    #on a le choix entre :
    #1 precisant: choix d'une porte,
    #les mots de passes valide associer a cette porte avec chacune des portes vers lesquelles il mene
    # si la porte est un gouffre et force l'agent a recommencer le labyrunthe
    # ou bien 2 le choix du boss
    # la concatenation des mot de passe depuis l'entre du labyrinthe pour le boss 
    #et le langage universel reconu par le boss
    #si le boss est vaincu ou non (si c'est non force l'agent a recommencer)

#facile
def afficher():
    t = True
    #interface console qui affiche :
    #entrer dans le labyrinthe (porte1)
    #ouvrir une porte
    #afficher le chemin parcouru (fonction qu'on a deja fait)
    #quitter

def lireInputMenu():
    valeur = input()
    if valeur.lower() not in ["a", "b", "c", "d"]:
        print("Index Invalide, reessayez:\n")
        valeur = "m"
    return valeur.lower()

def main():
    current = "m" # m -> "menu"
    while True:
        if current == "m":
            print("(a) Entrer dans le labyrinthe.")
            print("(b) Ouvrir une porte.")
            print("(c) Afficher le chemin parcouru.")
            print("(d) Quitter")
            current = lireInputMenu()
        elif current == "a":
            ouvrirPorte("Labyrinthe/Porte1.txt")
            current == "m"
        elif current == "b":
            numero = input("Entrer le numero de la porte : ")
            if numero == ("boss" or "Boss" or "BOSS"):
                ouvrirPorte("Labyrithe/Boss.txt", 0)
            else:
                ouvrirPorte("Labyrinthe/Porte" + numero + ".txt", numero)
            current = "m"
        elif current == "c":
            afficherLeCheminParcouru()
            current = "m"
        elif current == "d":
            break


if __name__ == "__main__":
    main()
