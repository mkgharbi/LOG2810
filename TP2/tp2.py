import random
from collections import defaultdict

terminaux = ["","a", "b", "c", "d", "e"]
nonTerminaux = ["A","B", "C", "D",  "S"]

currentPorte = "None"
States = []
inputs = []
nextState = []

porteArray = []  # TODO: Split as dictionnary??
gouffreArray = [] #TODO: Si une porte se trouve a etre un gouffre, on lajoute
passwordArray = [] # contenant les mots de passe dans chaque porte 
codeArray = [] # contenant les mots de passe valides 

chemins = defaultdict(list) # Cles: Les portes ouvertes, Valeurs: Tableau des portes essayes (Ex: {efedda, Porte6, valide})

def tryPorte(): #TODO: Find a way to append multiple doors
    index = random.randint(1, len(porteArray)) - 1
    tempPorte = porteArray[index]
    global chemins
    if checkPassword(tempPorte):
        afficher(tempPorte, True)
        ouvrirPorte(tempPorte+".txt", tempPorte)
        chemins[currentPorte].append([passwordArray[index], porteArray[index], "Valide"])
        return
    else:
        afficher(tempPorte, False)
        chemins[currentPorte].append([passwordArray[index], porteArray[index], "Non-valide"])
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
#def getMax(array):
 ##   maximum = len(array[0])
 #   for item in array: 
 #       if maximum < len(item) : 
  #          maximum = len(item)
  #  return maximum 

def fillTerminaux(etatFinaux, nonTerminauxPorte,arrayGrammar) : 
    for i in arrayGrammar:
        if i[1].size()==0:
            etatFinaux.append(i[0])
        if i[1].size() ==1:
            nonTerminauxPorte.append(i[1])



def genererCode(array,max):
    etatFinaux = set()
    #terminauxPorte =[] #lettre majuscule 
    nonTerminauxPorte = set() # lettre miniscule
    global codeArray 
    fillTerminaux(etatFinaux,nonTerminauxPorte,array)

    for code in passwordArray:
        if  code[code.length()-1] in nonTerminauxPorte :
            codeArray.append(code)
        

    returnArray = []
    return returnArray

def genererAutomate (array, porte):
    global passwordArray 
    global porteArray

    codeArray.clear()
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
    for key, value in chemins.items():
        print("Evenement Porte")
        print("a.   "+key)
        print("b.   ", end ="")
        for current in value:
            print(current, end = "")
        print()
        if key in gouffreArray:
            print("c.   Cette porte est un gouffre, retour a Porte1")
        else:
            print("c.   Cette porte n'est pas un gouffre")
    return

def afficher(porte, success):
    if currentPorte == "None":
        print("Vous etes maintenant a la porte 1 du Labyrinthe")
    elif success:
        print(porte+" ouverte")
    elif not success:
        print("Tentative d'ouvrir "+porte+" a echoué.")
        
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
            afficher("Porte1", True)
            ouvrirPorte("Porte1.txt", "Porte1")
            labyritheEntrer = True
            current = "m"
        elif current == "b":
            if labyritheEntrer:
                tryPorte()
            else:
                print("Veuillez entrer dans le labyrithe")
            current = "m"
        elif current == "c":
            afficherLeCheminParcouru()
            current = "m"
        elif current == "d":
            break


if __name__ == "__main__":
    main()
