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

arrayCodeBosse = []
arrayPorteBosse = []

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

def genererCodeBosse(arrayGrammar):
    codeBosse = arrayGrammar.size()
    arrayPorteBosse = codeBosse.split(" ")
    for i in arrayPorteBosse:
        #ce que je veux faire
        # c'est de chercher le nom de la porte ({efedda, Porte6, valide})
        # et prendre la premiere case de  {efedda, Porte6, valide} et la mettre dans
        #le arrayCodeBosse
        if arrayPorteBosse[i] in chemins[1]:  # ????est ce que ça fonctionne
            #est ce que il parcours tous le tableau des chemins
            arrayCodeBosse.append(chemins[0])


#def genererCodeBosse(arrayGrammar):
    #selon le chemin suivi 
    
    #  for i in range(0,len(chemins)):
    #     for j in chemins[i]:# changer avec for j in range(0,len(chemins[i]):
    #         for k in chemins[i][j][1]:
    #             if chemins[i+1] == k:
    #                 arrayCheminSuiviBosse.append(chemins[i][0])



# selon le fichier bosse
    codeBosse= arrayGrammar.size()
    arrayPorteBosse = codeBosse.split(" ")
    for i in range(0,len(arrayPorteBosse)-2):
        for porte in arrayPorteBosse:
            if "Boss" in porte: 
                for item in chemins[arrayPorteBosse[i]] : 
                    if (arrayPorteBosse[i+1] in chemins[arrayPorteBosse[i]][item][1]): 
                        arrayCodeBosse.append(chemins[arrayPorteBosse[i]][item][0])
        
        #for j in range(0,len(chemins[arrayPorteBosse[i]]-1)) :
            #if (arrayPorteBosse[i+1] in chemins[arrayPorteBosse[i]][j][1]): #and (chemins[arrayPorteBosse[i]][j][2] == "Valide"):

    # codeBosse = arrayGrammar.size()
    # arrayPorteBosse = codeBosse.split(" ")
    # for i in range(0,len(arrayPorteBosse)):
        #ce que je veux faire 
        # c'est de chercher le nom de la porte ({efedda, Porte6, valide})
        # et prendre la premiere case de  {efedda, Porte6, valide} et la mettre dans 
        #le arrayCodeBosse
    #    if arrayPorteBosse[i] in chemins [1]: #????est ce que ça fonctionne
    #        #est ce que il parcours tous le tableau des chemins 
    #       arrayCodeBosse.append(chemins[0])


alphabet =list(string.ascii_uppercase)

def genererLanguageBosee():

    # for item in arrayCodeBosse:
    #    arrayDebutDeCase.append(item[0])
    # for i in range(0,len(arrayDebutDeCase)): 
    # print("S-> "+arrayDebutDeCase[i]+alphabet[i]+arrayDebutDeCase.index(arrayDebutDeCase[i]))# objectif :c'est quelle affiche S-> eA1 si c'est dans la premiere case premiere lettre 
    for i in range(0,len(arrayCodeBosse)):
        for j in range(0,len(arrayCodeBosse[i])):
            if arrayCodeBosse[i][j] == arrayCodeBosse[i][0]:
                print("S-> "+arrayCodeBosse[i][0]+alphabet[i]+j)
            if arrayCodeBosse[i][j].size():#derniere case du tableau
                print(alphabet[i]+len(arrayCodeBosse[i])+"-> ")
                print(alphabet[i]+len(arrayCodeBosse[i])+"-> "+arrayCodeBosse[i][-1]+alphabet[i]+(j-1))
            else:
                print( alphabet[i]+j+"->"+arrayCodeBosse[i][j]+alphabet[i]+(j+1))

'''def genererLanguageBosee():

    # for item in arrayCodeBosse:
    #    arrayDebutDeCase.append(item[0])
    # # for i in range(0,len(arrayDebutDeCase)):
    # print("S-> "+arrayDebutDeCase[i]+alphabet[i]+arrayDebutDeCase.index(arrayDebutDeCase[i]))# objectif :c'est quelle affiche S-> eA1 si c'est dans la premiere case premiere lettre
    for i in range(0, len(arrayCodeBosse)):
        for j in range(0, len(arrayCodeBosse[i])):
            if arrayCodeBosse[i][j] == arrayCodeBosse[i][0]:
                print("S-> "+arrayCodeBosse[i][0]+alphabet[i]+j)
            if arrayCodeBosse[i][j].size():  # derniere case du tableau
                print(alphabet[i]+len(arrayCodeBosse[i])+"-> ")
                print(alphabet[i]+len(arrayCodeBosse[i])+"-> " +
                    arrayCodeBosse[i][-1]+alphabet[i]+(j-1))
            else:
                print(alphabet[i]+j+"->"+arrayCodeBosse[i]
                    [j]+alphabet[i]+(j+1))'''


def affronterLeBoss():
    t = True

    # lit la premiere ligne du fichier

    #on met chaque mot de passe de chaque porte dans une case d'un tableau (arrayPorteBosse)
    # on prend le  premier caractere de chaque case on met S-> premiercaratere A ,j'usqu'au dernier caractere (premiere case A , deuxieme case B .....)
    #on cherche la taille de chaque case
    # si la taille est de 1   S->premier caractere A1,  A1 ->
    #si la taille >1 on met pour le premier caractere S-> prermier caractere A1 , puis deuxieme caractere A1->deuxieme cacatere A2 j'usqu'au derniere caractere
    #on verifier si c'est le dernier par rapport a la taille de la case grace a la taille de mot de passe pour la premiere porte et on fait An-1 -> derniercar An
    # An->
    # aller a la derniere case dernier caractere et faire Zn-> , Zn-1 -> denrier caractere Zn jusqu'a on termine la derniere case puis aller a avant derniere case
    # Yn-> derniere caractere de Y (avant derniere case ) Z1
    # et on arrivant a la premiere case on fait S-> premier caractere de la case E
    # C'EST POUR GENERER LE LANGUAGE

    #lis le fichier Boss.txt
    #generer l'automate associé au chemin decrit dans le fichier
    #valider la concatenation des mot de passe des le debut
    #trouver le language

#Cette fonction affiche l'historique du chemin parcouru
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
