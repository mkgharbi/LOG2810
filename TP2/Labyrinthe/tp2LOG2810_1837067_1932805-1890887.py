import string

terminaux = ["","a", "b", "c", "d", "e"]
nonTerminaux = ["A","B", "C", "D",  "S"]

currentPorte = "None" #porte Courante. 
parcours = [] #Historique des portes visitees
chemins = [] #Chemins possibles d'une porte (Index de parcours -> Index de chemins)
currentPath = []

porteArray = []  # Portes accessibles a partir de la porte courrente
passwordArray = [] # Mots de passes de la porte courante
grammar = [] # Grammaire de la porte courante

gouffreArray = [] # Si une porte se trouve a etre un gouffre, on lajoute.
validPasswords = [] # contenant les mots de passe valides.
validDoors = [] #contenant les portes valides reliees aux mots de passe valides.

etatsFinaux = set() #etats finaux
terminauxPorte = set() #terminaux de la porte courrante

alphabet = list(string.ascii_uppercase) #toute l'alphabet 
arrayCodeBoss = [] #Les codes pour le boss
arrayPorteBoss = [] #Les portes pour arriver au boss
arrayPorteBossMem = [] #Pour garder les portes du boss en memoire

# Cette fonction verifie que le mot de passe la porte passée en parametre est bel et bien accessible
def checkPassword(porte):
    position = porteArray.index(porte)
    if passwordArray[position] in validPasswords:
        return True 
    return False  

# C1) Cette fonction est appelé dès que l'on a confirmer que la porte voulus est accessible
def ouvrirPorte(fichier): 
    global currentPorte
    global porteArray
    global passwordArray
    global validPasswords
    global validDoors
    global parcours
    global currentPath
    porte = fichier[0:fichier.index(".")] #substring 
    if porte == "Porte1":
        currentPath.clear() 
    currentPorte = porte
    parcours.append(currentPorte)
    currentPath.append(currentPorte)

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

# C3) Cette fonction génère l'automate qui verifie qu'un mot de passe est bel et bien valide
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
    fillTables(grammar) #Remplir les etats.
    validMotDePasse(grammar) # Remplir les mots de passes valides et les portes valides. 
    estGouffre() #remplir tableau des gouffres 
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
            if terminal == item[1][0] and item[1][len(item[1])-1] in etatsFinaux: 
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
    if len(chemins[parcours.index(currentPorte)]) < 1 : 
        for porte in porteArray:
                position = porteArray.index(porte)
                if checkPassword(porte) :
                    chemins[parcours.index(currentPorte)].append([passwordArray[position], porteArray[position], "Valide"])
                else : 
                    chemins[parcours.index(currentPorte)].append([passwordArray[position], porteArray[position], "Non-valide"])

# Cette fonction essaye d'ouvrir la porte que l'utilisateur a spécifié
def tryPorte(numero): 
    porte = "Porte" + numero
    position = porteArray.index(porte)
    tempPorte = porteArray[position]
    global chemins
    if checkPassword(tempPorte):
        afficherEtMettreAjour(tempPorte, True)
        ouvrirPorte(tempPorte+".txt")
        fillChemins()
        if tempPorte in gouffreArray:
            print("Cette porte est un gouffre. Retour à la porte1!")
            return
        print(chemins[parcours.index(tempPorte)])
        
    else:
        afficherEtMettreAjour(tempPorte, False)
    return

# Cette fonction concatene les mots de passe precedents
def genererCodeBoss():
    global arrayPorteBossMem
    ligne = open("Boss.txt", "r")
    lesPortes = ligne.readline()
    arrayPorteBoss = lesPortes.split(" ")
    arrayPorteBossMem = arrayPorteBoss
    arrayPorteBoss.pop()

    for i in currentPath:
        tempPorte = chemins[parcours.index(i)]
        for j in tempPorte:
            if currentPath.index(i) < len(arrayPorteBoss) - 1:
                if arrayPorteBoss[currentPath.index(i)+1] == j[1]:
                    arrayCodeBoss.append(j[0])

    for item in arrayCodeBoss:
        print(str(item))

# Cette fonction genere le langage que le Boss comprend a partir de la concatenation des mots de passe
def genererLanguageBoss():
    print()
    for i in range(0, len(arrayCodeBoss)):
        for j in range(0, len(arrayCodeBoss[i])):
            if arrayCodeBoss[i][j] == arrayCodeBoss[i][0]:
                print("S->"+arrayCodeBoss[i][0]+alphabet[i]+str(j),end=" ")
                if arrayCodeBoss[i][j] ==arrayCodeBoss[i][len(arrayCodeBoss[i])-1]:
                    print(alphabet[i]+str(len(arrayCodeBoss[i])-1) +"->S",end=" ")
            if arrayCodeBoss[i][j] ==arrayCodeBoss[i][len(arrayCodeBoss[i])-1] and arrayCodeBoss[i][j] != arrayCodeBoss[i][0]:  # derniere case du tableau !! a corriger 
                print(str(alphabet[i])+str(len(arrayCodeBoss[i])-2)+"->"+arrayCodeBoss[i][j]+alphabet[i]+str(len(arrayCodeBoss[i])-1),end=" ")
                print(alphabet[i]+str(len(arrayCodeBoss[i])-1) +"->S",end=" ")
            if arrayCodeBoss[i][j] != arrayCodeBoss[i][0] and  arrayCodeBoss[i][j] !=arrayCodeBoss[i][len(arrayCodeBoss[i])-1]:
                k=j-1
                print(alphabet[i]+str(k)+"->"+str(arrayCodeBoss[i][j])+alphabet[i]+str((j)),end=" ")
    print ("S->")

#C2) Cette fonction nous permet d'affronter le bpss
def affronterLeBoss():
    genererCodeBoss()
    genererLanguageBoss()


#C4) Cette fonction affiche l'historique du chemin parcouru
def afficherLeCheminParcouru():
    print()
    for i in parcours:
        if i != "Boss":
            print("Evenement Porte")
        else:
            print("Evenementt Boss")
        print()
        if i != "Boss":
            print("a.   ", i)
        else:
            print("a.   ", end="")
            for j in arrayPorteBossMem:
                print(j, end=" ")
            print(end="\n")

        if i != "Boss":
            print("b.   ", chemins[parcours.index(i)])
        else:
            print("b.   ", arrayCodeBoss)

        if i in gouffreArray and i != "Boss":
            print("c.   Cette porte est un gouffre, retour a Porte1.")
            print()
            ouvrirPorte("Porte1.txt")
        else:
            if i != "Boss":
                print("c.   Cette porte n'est pas un gouffre")
                print()

        if i == "Boss":
            print("c.   Vous avez vaincu le Boss!!!")
            print()
    

# Cette fonction affiche de l'information en fonction de la situation
def afficherEtMettreAjour(porte, success):
    global currentPorte
    global currentPath
    if currentPorte == "None":
        print("Vous etes maintenant a la porte 1 du Labyrinthe")
    elif success:
        print(porte+" ouverte")

    elif not success:
        print("Tentative d'ouvrir "+porte+" a echoué.")
        print("Vous etes retourne a la Porte 1")
        currentPath.clear()
        ouvrirPorte("Porte1.txt")
        fillChemins()

#Clear tout les tableaux
def clearLab():
    global currentPorte
    currentPorte = "None"
    parcours.clear() 
    chemins.clear() 
    currentPath.clear()
    porteArray.clear()  
    passwordArray.clear()
    grammar.clear()
    gouffreArray.clear() 
    validPasswords.clear() 
    validDoors.clear() 
    etatsFinaux.clear()
    terminauxPorte.clear()
    arrayCodeBoss.clear()
    arrayPorteBoss.clear()
    arrayPorteBossMem.clear()

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
            #C5) L'interface console :
            print("(a) Entrer dans le labyrinthe.")
            print("(b) Ouvrir une porte.")
            print("(c) Afficher le chemin parcouru.")
            print("(d) Quitter")
            current = lireInputMenu()

        elif current == "a":
            clearLab()
            afficherEtMettreAjour("Porte1", True)
            ouvrirPorte("Porte1.txt")
            fillChemins()
            print(chemins)
            labyrintheEntrer = True
            bossTuer = False
            current = "m"

        elif current == "b":
            if labyrintheEntrer and not bossTuer:
                numero = input("Numero de la porte ?")
                if numero.isdigit():
                    if int(numero) >= 0 and int(numero) <=20 : 
                        nomPorte = "Porte" + numero
                        if nomPorte in porteArray:
                            tryPorte(numero)
                            fillChemins()
                        else :
                            ouvrirPorte("Porte1.txt")
                            fillChemins()
                elif numero in ["boss","Boss","BOSS"]:
                    parcours.append("Boss")
                    chemins.append(["Ceci est le Boss"])
                    affronterLeBoss()
                    print("Vous avez vaincu le Boss")
                    bossTuer = True
                else:
                    ouvrirPorte("Porte1.txt")
                    fillChemins()
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


