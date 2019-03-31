import random
from collections import defaultdict

# je pense qu'on n'a pas besoin de ces deux tableau ??????
terminaux = ["","a", "b", "c", "d", "e"]
nonTerminaux = ["A","B", "C", "D",  "S"]

currentPorte = "None" #porte Courante. 
parcours = []

porteArray = []  # TODO: Split as dictionnary??
gouffreArray = [] #TODO: Si une porte se trouve a etre un gouffre, on lajoute.
passwordArray = [] # contenant les mots de passe dans chaque porte. 
validPasswords = [] # contenant les mots de passe valides.
validDoors = [] #contenant les portes valides reliees aux mots de passe valides.
# je pense qu'il faut changé le nom ????????????? est ce que lesPossibiliter ce'est bon ???????
chemins = defaultdict(list) # Cles: Les portes ouvertes, Valeurs: Tableau des portes essayes (Ex: {efedda, Porte6, valide})
grammar = [] # grammaire 

etatsFinaux = set()
nonTerminauxPorte = set()


def checkPassword(porte):
    position = porteArray.index(porte)
    if passwordArray[position] in validPasswords:
        return True 
    return False  

def ouvrirPorte(fichier):  # TODO: update currentPorte & read all the file in one function : 
    #TODO : return the valid doors. 
    global currentPorte
    global porteArray
    global passwordArray
    global validPasswords
    global validDoors
    porte = fichier[0:fichier.index(".")] #substring 
    
    currentPorte = porte
    parcours.append(currentPorte)

    porteFile = open(fichier, "r")
    porteFile.readline() # ignore the { 
    tempGrammar = porteFile.readline().strip("\n") #Read only the grammar. 
    tempGrammar.rstrip()
    arrayGrammar = tempGrammar.split(", ") #split it in a table

    porteFile.readline() # ignore the } 
    tempArray = []
    #Read the next lines : 
    while True:
        currentLine = porteFile.readline().strip("\n")
        if not currentLine: #not the end of the file. 
            break
        currentLineArray = currentLine.split(" ") # split each line (password PorteX)
        if len(currentLineArray) >= 2: #if there's a password 
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
    genererAutomate(arrayGrammar, porte) #generate the automate depending on the grammar : separate the valid passwords & put them in the table validPasswords. 
    return validDoors


#TODO : genererAutomate () : 
def genererAutomate(array, porte):

    global passwordArray
    global porteArray
    global validDoors
    validPasswords.clear()  # clear the ancient valid passwords.
    validDoors.clear()
    tempArray = []
    for item in array:
        grammar = item.split("->")
        tempArray.append(grammar)  
    grammar = tempArray
    fillTables(grammar)
    validMotDePasse(grammar)    
    return

# fillTables :
def fillTables(grammar):
    global etatsFinaux
    global nonTerminauxPorte

    for items in grammar:
        if len(items[1]) == 0:
            etatsFinaux.add(items[0])
        if len(items[1]) == 1 or items[1][len(items[1])-1] ==" ":
            nonTerminauxPorte.add(items[1][0])

#: estGouffre  :
def estGouffre():
    global gouffreArray
    if len(etatsFinaux) == 0 and len(nonTerminauxPorte) == 0:
        gouffreArray.append(currentPorte)

def findNonTerminal(nonTerminal,arrayGrammar):
    for item in arrayGrammar:
        if nonTerminal in nonTerminauxPorte:
            return True
        if len(item[1]) == 0 : 
                return 
        if item[1][len(item[1])-1] in etatsFinaux:
            return True
        if nonTerminal == item[1][0] and item[1][len(item[1])-1] in etatsFinaux:
            return True
    return False

def validMotDePasse(arrayGrammar):
    global validPasswords
    global validDoors

    for code in passwordArray:
        if (code[len(code)-1] in nonTerminauxPorte) or (findNonTerminal(code[len(code)-1],arrayGrammar)):
            validPasswords.append(code)
            validDoors.append(porteArray[passwordArray.index(code)])

def fillChemins():
    global chemins
    for porte in porteArray:
            position = porteArray.index(porte)
            if checkPassword(porte) :
                chemins[currentPorte].append([passwordArray[position], porteArray[position], "Valide"])
            else : 
                chemins[currentPorte].append([passwordArray[position], porteArray[position], "Non-valide"])



def tryPorte(numero): #TODO: Find a way to append multiple doors
    porte = "Porte" + numero
    position = porteArray.index(porte)
    tempPorte = porteArray[position]
    global chemins
    if checkPassword(tempPorte):
        afficher(tempPorte, True)
        ouvrirPorte(tempPorte+".txt")
    else:
        afficher(tempPorte, False)
        
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
        print("Evenement Porte")
        print("a.   " + parcours[len(parcours)-1])
        print()
        print("b.   " + str(chemins[parcours[len(parcours)-1]])
        print()
        if parcours[len(parcours)-1] in gouffreArray:
            print("c.   Cette porte est un gouffre, retour a Porte1")
        else:
            print("c.   Cette porte n'est pas un gouffre")

def afficher(porte, success):
    global currentPorte
    if currentPorte == "None":
        print("Vous etes maintenant a la porte 1 du Labyrinthe")
    elif success:
        print(porte+" ouverte")

    elif not success:
        print("Tentative d'ouvrir "+porte+" a echoué.")
        currentPorte = "Porte1"
        
        print("Vous etes retourne a la Porte 1 , veuillez appuyer sur b")
        
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
            fillChemins()
            print(chemins)
            labyritheEntrer = True
            current = "m"
        elif current == "b":
            if labyritheEntrer:
                afficherLeCheminParcouru()
                numero = input("Numero de la porte ?")
                nomPorte = "Porte" + numero
                if nomPorte in porteArray:
                    tryPorte(numero)
                else :
                    currentPorte = "Porte1"
                    print("Vous êtes revenu à la Porte 1. Ressayez.")
                    chemins.clear()
                
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
