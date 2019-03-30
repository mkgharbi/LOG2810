import random
from collections import defaultdict

# je pense qu'on n'a pas besoin de ces deux tableau ??????
terminaux = ["","a", "b", "c", "d", "e"]
nonTerminaux = ["A","B", "C", "D",  "S"]

currentPorte = "None"

porteArray = []  # TODO: Split as dictionnary??
gouffreArray = [] #TODO: Si une porte se trouve a etre un gouffre, on lajoute.
passwordArray = [] # contenant les mots de passe dans chaque porte. 
validPasswords = [] # contenant les mots de passe valides.
validDoors = [] #contenant les portes valides reliees aux mots de passe valides.
# je pense qu'il faut changé le nom ????????????? est ce que lesPossibiliter ce'est bon ???????
chemins = defaultdict(list) # Cles: Les portes ouvertes, Valeurs: Tableau des portes essayes (Ex: {efedda, Porte6, valide})


etatsFinaux = set()
nonTerminauxPorte = set()





def checkPassword(porte):
    if validPasswords.index(passwordArray[porteArray.index(porte)]) >= 0:
        return True 
    return False  

def fillChemins(numero):
    global chemins 
    for current in porteArray: 
        index = porteArray.index(current)
        if checkPassword(current) : 
            chemins[currentPorte].append([passwordArray[index], current, "Valide"])
        else :  
            chemins[currentPorte].append([passwordArray[index], current, "Non-valide"])


def ouvrirPorte(fichier):  # TODO: update currentPorte & read all the file in one function : 
    #TODO : return the valid doors. 
    global currentPorte
    global porteArray
    global passwordArray
    global validPasswords
    global validDoors

    porte = fichier[0:fichier.index(".")-1] #substring 
    currentPorte = porte
    porteFile = open(fichier, "r")
    porteFile.readline() # ignore the { 
    tempGrammar = porteFile.readline().strip("\n") #Read only the grammar. 
    arrayGrammar = tempGrammar.split(", ") #split it in a table 
    porteFile.readline() # ignore the } 

    tempArray = []
    #Read the next lines : 
    while True:
        currentLine = porteFile.readline().strip("\n")
        if not currentLine: #not the end of the file. 
            break
        currentLineArray = currentLine.split(" ") # split each line (password PorteX)
        if len(currentLineArray) == 2: #if there's a password 
            tempArray.append(currentLineArray[0])
            tempArray.append(currentLineArray[1])
        elif currentLineArray == 1: # if there isn't a password.
            tempArray.append("")
            tempArray.append(currentLineArray[0])
    #clear the ancient values in the tables. 
    passwordArray.clear()
    porteArray.clear()
    for current in tempArray: # separate passwords and PorteX in the current table.  
        if "Porte" in current:
            porteArray.append(current) # all the passwords connectec with the doors.
        else:
            passwordArray.append(current) # the current doors. 

    tempArray.clear() #clear the temporary table. 
    validPasswords.clear() # clear the ancient valid passwords. 
    validPasswords.append("")
    validDoors.clear() 
    genererAutomate(arrayGrammar, porte) #generate the automate depending on the grammar : separate the valid passwords & put them in the table validPasswords. 
    return validDoors


#TODO : genererAutomate () : 
def genererAutomate(array, porte):
    global passwordArray
    global porteArray
    global validDoors
    tempArray = []
    for item in array:
        grammar = item.split("->")
        tempArray.append(grammar)
    
    fillTables(tempArray)

    validMotDePasse(tempArray)

    
    return


# fillTables :
def fillTables(array):
    global etatsFinaux
    global nonTerminauxPorte

    for item in array:
        if len(item[1]) == 0:
            etatsFinaux.add(item[0])
        if len(item[1]) == 1:
            nonTerminauxPorte.add(item[1])


#: estGouffre  :
def estGouffre(etatfinaux, nonTerminauxPorte):
    if len(etatfinaux) == 0 and len(nonTerminauxPorte) == 0:
        return True
    return False



def findNonTerminal(nonTerminal,arrayGrammar):
    for item in arrayGrammar:
        if (nonTerminal in nonTerminauxPorte) or (item[2][1] in etatsFinaux) or (nonTerminal == item[2][0] and item[2][1] in etatsFinaux):
            return True
    return False

def validMotDePasse(arrayGrammar):
    global validPasswords
    global validDoors

    for code in passwordArray:
        if (code[len(code)-1] in nonTerminauxPorte) or (findNonTerminal(code[len(code)-1],arrayGrammar)):
            validPasswords.append(code)
            validDoors.append(porteArray[passwordArray.index(code)])



def tryPorte(numero): #TODO: Find a way to append multiple doors
    index = porteArray.index("Porte"+numero)
    tempPorte = porteArray[index]
    global chemins
    if checkPassword(tempPorte):
        afficher(tempPorte, True)
        ouvrirPorte(tempPorte+".txt")
        chemins[currentPorte].append([passwordArray[index], porteArray[index], "Valide"])
    else:
        afficher(tempPorte, False)
        chemins[currentPorte].append([passwordArray[index], porteArray[index], "Non-valide"])
        
    print(chemins[tempPorte])
    return


#moyen
def affronterLeBoss():
    t = True
    #lis le fichier Boss.txt
    #generer l'automate associé au chemin decrit dans le fichier 
    #valider la concatenation des mot de passe des le debut 
    #trouver le language




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
            afficher("Porte1", True)
            ouvrirPorte("Porte1.txt")
            labyritheEntrer = True
            current = "m"
        elif current == "b":
            if labyritheEntrer:
                afficherLeCheminParcouru()
                numero = input("Numero de la porte ?")
                tryPorte(numero)
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
