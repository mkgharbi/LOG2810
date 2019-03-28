import random

terminaux = ["","a", "b", "c", "d", "e"]
nonTerminaux = ["A","B", "C", "D",  "S"]

currentPorte = "None"
States = []
inputs = []
nextState = []

porteArray = []  # TODO: Split as dictionnary??
passwordArray = []
codeArray = []

chemins = dict() # Cles: Les portes ouvertes, Valeurs: Tableau des portes essayes (Ex: {efedda, Porte6, valide})

def tryPorte(): #TODO: Sauvegarder les chemins selon le standard du dictionaire ci-haut
    tempPorte = porteArray[random.randint(1, len(porteArray)) - 1]
    if checkPassword(tempPorte):
        afficher(tempPorte, True)
        ouvrirPorte(tempPorte+".txt", tempPorte)
        return
    else:
        afficher(tempPorte, False)
        return
   
def ouvrirPorte (fichier, porte): #TODO: update porte courrante
    global currentPorte
    currentPorte = porte
    porteFile = open(fichier, "r")
    porteFile.readline()
    tempGrammar = porteFile.readline().strip("\n")
    arrayGrammar = tempGrammar.split(", ")
    genererAutomate(arrayGrammar, porte)
    return

#moyen
def affronterLeBoss():
    t = True
    #lis le fichier Boss.txt
    #generer l'automate associé au chemin decrit dans le fichier 
    #valider la concatenation des mot de passe des le debut 
    #trouver le language

#moyen
def getMax(array):
    maximum = len(array[0])
    for item in array: 
        if maximum < len(item) : 
            maximum = len(item)
    return maximum 

def genererCode(array,max):
    returnArray = []
    return returnArray

def genererAutomate (array, porte):
    passwordArray.clear()
    porteArray.clear()
    tempArray = []
    porteFile = open(porte+".txt", "r")
    porteFile.readline()
    porteFile.readline()
    porteFile.readline()
    while True:
        currentLine = porteFile.readline().strip("\n")
        if not currentLine:
            break
        currentLineArray = currentLine.split(" ")
        tempArray.append(currentLineArray[0])
        tempArray.append(currentLineArray[1])
    for current in tempArray: #separe les mots de passes et les portes
        print
        if "Porte" in current:
            porteArray.append(current)
        else:
            passwordArray.append(current)
    tempArray.clear()
    global codeArray
    codeArray.clear()
    codeArray = genererCode(array, getMax(passwordArray))
    codeArray.append("")
    return

def checkPassword(porte):
    passwordFound = False
    for current in codeArray:
        if current == passwordArray[porteArray.index(porte)]:
            passwordFound = True
            break
    return passwordFound

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
def afficher(porte, success):
    if currentPorte == "None":
        print("Vous etes maintenant a la porte 1 du Labyrinthe")
    elif success:
        print(porte+" ouverte")
    elif not success:
        print("Tentative d'ouvrir "+porte+" a echouer.")
        
def lireInputMenu():
    valeur = input()
    if valeur.lower() not in ["a", "b", "c", "d"]:
        print("Index Invalide, reessayez:\n")
        valeur = "m"
    return valeur.lower()

def main():
    labyritheEntrer = False
    bossTuer = False
    current = "m" # m -> "menu"
    while True:
        if current == "m":
            print("(a) Entrer dans le labyrinthe.")
            print("(b) Ouvrir une porte.")
            print("(c) Afficher le chemin parcouru.")
            print("(d) Quitter")
            current = lireInputMenu()
        elif current == "a":
            ouvrirPorte("Porte1.txt", "Porte1")
            labyritheEntrer = True
            current = "m"
        elif current == "b":
            tryPorte()
            current = "m"
        elif current == "c":
            afficherLeCheminParcouru()
            current = "m"
        elif current == "d":
            break


if __name__ == "__main__":
    main()
