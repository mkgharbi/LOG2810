import random
import string
from collections import defaultdict

terminaux = ["","a", "b", "c", "d", "e"]
nonTerminaux = ["A","B", "C", "D",  "S"]

currentPorte = "None" #porte Courante. 
parcours = [] #Historique des portes visitees
chemins = [] #Chemins possibles d'une porte (Index de parcours -> Index de chemins)

porteArray = []  # Portes accessibles a partir de la porte courrente
passwordArray = [] # Mots de passes de la porte courante
grammar = [] # Grammaire de la porte courante

gouffreArray = [] # Si une porte se trouve a etre un gouffre, on lajoute.
validPasswords = [] # contenant les mots de passe valides.
validDoors = [] #contenant les portes valides reliees aux mots de passe valides.

etatsFinaux = set()
terminauxPorte = set()

arrayCodeBoss = []
arrayPorteBoss = []

# Cette fonction verifie que le mot de passe la porte passée en parametre est bel et bien accessible
def checkPassword(porte):
    position = porteArray.index(porte)
    if passwordArray[position] in validPasswords:
        return True 
    return False  

#def ouvrirPorteBoss():
 #   ligne = open("Boss.txt","r")
 #   ligne.readline()
    

# C1) Cette fonction est appelé dès que l'on a confirmer que la porte voulus est accessible
def ouvrirPorte(fichier): 
    global currentPorte
    global porteArray
    global passwordArray
    global validPasswords
    global validDoors
    porte = fichier[0:fichier.index(".")] #substring 
    
    currentPorte = porte
    parcours.append(currentPorte)
    chemins.append([])

    porteFile = open(fichier, "r")
    porteFile.readline() # ignore the { 
    tempGrammar = porteFile.readline().strip("\n") #Read only the grammar. 
    tempGrammar.rstrip()
    arrayGrammar = tempGrammar.split(", ") #split into a table
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

    #clear the ancient values in the lists
    passwordArray.clear()
    porteArray.clear()
    for current in tempArray: # separate passwords and PorteX in the current table.  
        if "Porte" in current or "Boss" in current:
            porteArray.append(current) # all the passwords connectec with the doors.
        else:
            passwordArray.append(current) # the current doors. 

    tempArray.clear() #clear the temporary table. 
    genererAutomate(arrayGrammar, porte) #generate the automate depending on the grammar : separate the valid passwords & put them in the table validPasswords. 
    return validDoors

# C2) Cette fonction génère l'automate qui verifie qu'un mot de passe est bel et bien valide
def genererAutomate(array, porte):
    global passwordArray
    global porteArray
    global validDoors
    validPasswords.clear()  # clear the ancient lists
    validDoors.clear()
    tempArray = []
    for item in array:
        grammar = item.split("->")
        tempArray.append(grammar)  
    grammar = tempArray
    fillTables(grammar)
    validMotDePasse(grammar)    
    return

# Cette fonction remplie la table des etats finaux voulus et des terminaux trouvés dans la grammaire
def fillTables(grammar):
    global etatsFinaux
    global terminauxPorte
    etatsFinaux.clear()
    terminauxPorte.clear()
    for items in grammar:
        if len(items[1]) == 0:
            etatsFinaux.add(items[0])
        if len(items[1]) >= 1 :
            if (len(items[1]) == 1) or (len(items[1]) == 2 and items[1][1] == " "):
                terminauxPorte.add(items[1][0])

# Cette fonction verifie si une porte est un gouffre afin que l'on puisse le savoir lors de l'affichage
def estGouffre():
    global gouffreArray
    if len(etatsFinaux) == 0 and len(terminauxPorte) == 0:
        gouffreArray.append(currentPorte)

# Cette fonction confirme la presence d'une chaine completée
def findTerminal(terminal,arrayGrammar):
    for item in arrayGrammar:
        if terminal in terminauxPorte:
            return True
        if len([item[1]]) - 1 > 0:
            if item[1][len(item[1])-1] in etatsFinaux:
                return True
            if terminal == item[1][0] and item[1][len(item[1])-1] in etatsFinaux: # TODO : check another condition when a terminal lets us go to a final state. Like : S is in etatsFinaux and S->eS (e leads us to S)
                return True
        for anotherItem in arrayGrammar: #Pour chaque item de arrayGrammar, on itere encore une fois pour voir s'il y a un cas du type S-> , S->eS
            if len(anotherItem[1]) >= 2:
                if (item[1] is "") and (anotherItem[1][len(anotherItem[1]) - 1] == item[0]):
                    if anotherItem[1][len(anotherItem[1]) - 2] == terminal:
                        return True
                    elif len(item[1]) >= 2:
                        if item[1][len(item[1]) - 2] == terminal:
                            return True
                        else:
                            return False
    return False

#Cette fonction verifie qu'un mot de passe peut etre generer a partie de la gramaire passée en parametre
def validMotDePasse(arrayGrammar):
    global validPasswords
    global validDoors
    for code in passwordArray:
        if len(code) > 0:
            if (findTerminal(code[len(code)-1],arrayGrammar)):
                validPasswords.append(code)
                validDoors.append(porteArray[passwordArray.index(code)])
        else:
            for current in arrayGrammar:
                if current[0] == "S":
                    validPasswords.append(code)
                    validDoors.append(porteArray[passwordArray.index(code)])

# Cette fonction ajoute les portes a une liste qui nous permettra d'acceder aux details du parcours (soit la liste parcours)
def fillChemins():
    global chemins
    for porte in porteArray:
            position = porteArray.index(porte)
            if checkPassword(porte) :
                chemins[parcours.index(currentPorte)].append([passwordArray[position], porteArray[position], "Valide"])
            else : 
                chemins[parcours.index(currentPorte)].append([passwordArray[position], porteArray[position], "Non-valide"])

# Cette fonction essaye d'ouvrir la porte que l'utilisateur a spécifié
def tryPorte(numero): #TODO: Find a way to append multiple doors
    porte = "Porte" + numero
    position = porteArray.index(porte)
    tempPorte = porteArray[position]
    global chemins
    if checkPassword(tempPorte):
        afficher(tempPorte, True)
        ouvrirPorte(tempPorte+".txt")
        fillChemins()
        print(chemins[parcours.index(tempPorte)])
    else:
        afficher(tempPorte, False)
        parcours.append("Porte1")
        
    return

def genererCodeBoss():
    ligne = open("Boss.txt","r")
    lesPortes=ligne.readline()
    arrayPorteBoss = lesPortes.split(" ")
    
# selon le fichier boss
    #codeBoss= arrayGrammar.size()
   # arrayPorteBoss = codeBoss.split(" ")
    for i in range(0,len(arrayPorteBoss)-3):
        for j in range(0,len(chemins[i])) :
            if arrayPorteBoss[i+1] in chemins[i][j][1]:
                  arrayCodeBoss.append(chemins[i][j][0])
                
      #  for porte in arrayPorteBoss:
       #     for item in chemins[i] : #arrayPorteBoss
       #         if (arrayPorteBoss[i+1] in chemins[i][item][1]): # chemins[arrayPorteBoss[i]][item][1
                      #arrayCodeBoss.append(chemins[arrayPorteBoss[i]][item][0])
        


alphabet =list(string.ascii_uppercase)

def genererLanguageBoss():

    for i in range(0,len(arrayCodeBoss)):
        for j in range(0,len(arrayCodeBoss[i])):
            if arrayCodeBoss[i][j] == arrayCodeBoss[i][0]:
                print("S-> "+arrayCodeBoss[i][0]+alphabet[i]+str(j))
            if len(arrayCodeBoss[i][j]):#derniere case du tableau
                print(str(alphabet[i])+str(len(arrayCodeBoss[i]))+"-> ")
                
                print(alphabet[i]+str(len(arrayCodeBoss[i]))+"-> "+arrayCodeBoss[i][-1]+alphabet[i]+str((j-1)))
            else:
                print( alphabet[i]+j+"->"+arrayCodeBoss[i][j]+alphabet[i]+(j+1))



def affronterLeBoss():
    genererCodeBoss()
    genererLanguageBoss()

def afficherLeCheminParcouru():
    for i in parcours:
        print("Evenement Porte")
        print()
        print("a.   ", i)
        print("b.   ", chemins[parcours.index(i)])
        if parcours[len(parcours)-1] in gouffreArray:
            print("c.   Cette porte est un gouffre, retour a Porte1")
        else:
            print("c.   Cette porte n'est pas un gouffre")

# Cette fonction affiche de l'information en fonction de la situation
def afficher(porte, success):
    global currentPorte
    if currentPorte == "None":
        print("Vous etes maintenant a la porte 1 du Labyrinthe")
    elif success:
        print(porte+" ouverte")

    elif not success:
        print("Tentative d'ouvrir "+porte+" a echoué.")
        currentPorte = "Porte1"
        print("Vous etes retourne a la Porte 1")

# Cette fonction verifie les entrés de l'utilisateur lors de la navigation du menu
def lireInputMenu():
    valeur = input()
    if valeur.lower() not in ["a", "b", "c", "d"]:
        print("Index Invalide, reessayez:\n")
        valeur = "m"
    return valeur.lower()

# main
def main():
    global currentPorte
    
    labyrintheEntrer = False
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
            labyrintheEntrer = True
            current = "m"

        elif current == "b":
            if labyrintheEntrer:
                numero = input("Numero de la porte ?")
                nomPorte = "Porte" + numero
                if nomPorte in porteArray:
                    tryPorte(numero)
                elif numero in ["boss","Boss","BOSS"]:
                    affronterLeBoss()
                #else:
                #    print("Invalide")
                else :
                    currentPorte = "Porte1"
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
