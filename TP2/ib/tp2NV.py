import random
import string
from collections import defaultdict

# je pense qu'on n'a pas besoin de ces deux tableau ??????
terminaux = ["","a", "b", "c", "d", "e"]
nonTerminaux = ["A","B", "C", "D",  "S"]

currentPorte = "None"
doorsArray = set()

inputs = [] # est ce que c'est necessaire ????????
nextState = [] # on ne l'as pas utilisé est ce que c'est important ??????

porteArray = []  # TODO: Split as dictionnary??
gouffreArray = [] #TODO: Si une porte se trouve a etre un gouffre, on lajoute
passwordArray = [] # contenant les mots de passe dans chaque porte 
validPasswords = [] # contenant les mots de passe valides 

# je pense qu'il faut changé le nom ????????????? est ce que lesPossibiliter ce'est bon ???????
chemins = defaultdict(list) # Cles: Les portes ouvertes, Valeurs: Tableau des portes essayes (Ex: {efedda, Porte6, valide})


# je pense qu'il veut mieux changer cette methode on peut je pense la fusionner avec checkmotdepasse


def checkPassword(porte):
    if validPasswords.index(passwordArray[porteArray.index(porte)]) >= 0:
        return True 
    return False 

def tryPorte(numero): #TODO: Find a way to append multiple doors
    index = porteArray.index("Porte"+numero)
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
arrayCodeBosse=[]
arrayPorteBosse = []

def genererCodeBosse(arrayGrammar):
    codeBosse = arrayGrammar.size()
    arrayPorteBosse = codeBosse.split(" ")
    for i in  arrayPorteBosse:
        #ce que je veux faire 
        # c'est de chercher le nom de la porte ({efedda, Porte6, valide})
        # et prendre la premiere case de  {efedda, Porte6, valide} et la mettre dans 
        #le arrayCodeBosse
        if arrayPorteBosse[i] in chemins [1]: #????est ce que ça fonctionne
            #est ce que il parcours tous le tableau des chemins 
            arrayCodeBosse.append(chemins[0])

#arrayDebutDeCase=[]
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

#moyen
#def getMax(array):
##   maximum = len(array[0])
#   for item in array: 
#       if maximum < len(item) : 
#          maximum = len(item)
#  return maximum 


#a fillTables :  
def fillTables(etatFinaux,nonTerminauxPorte,array) : 
    for i in array:
        if i[1].size()==0:
            etatFinaux.append(i[0])
        if i[1].size() == 1:
            nonTerminauxPorte.append(i[1])

#: estGouffre  : 
def estGouffre(etatfinaux, nonTerminauxPorte):
    if len(etatfinaux) == 0 and len(nonTerminauxPorte) == 0 : 
        return True 
    return False 

# motdePasse valide : 
def findNonTerminal(nonTerminal,etatFinaux,nonTerminauxPorte, arrayGrammar): 
    for item in arrayGrammar :
        if nonTerminal in nonTerminauxPorte:
            return True
        if nonTerminal == item[2][0] and item[2][1] in etatFinaux : 
            return True
        if item[2][1] in etatFinaux : 
            return True 
    return False

def validMotDePasse(etatsFinaux, nonTerminauxPorte,passwordArray,arrayGrammar):
    global porteArray
    global validPasswords

    for code in passwordArray:
        if  code[len(code)-1] in nonTerminauxPorte :
            validPasswords.append(code)
        else :
            if findTerminal(code[len(code)-1],etatsFinaux,nonTerminauxPorte, arrayGrammar):
                validPasswords.append(code)


def genererCode(array):
    for item in array : 
        grammar = item.split("->")
    
    etatFinaux = set()
    nonTerminauxPorte = set() # lettre miniscule
    global passwordArray 
    global porteArray
    global validPasswords
    fillTables(etatFinaux,nonTerminauxPorte,grammar)
    validMotDePasse(etatFinaux,nonTerminauxPorte,passwordArray,grammar)

#TODO : genererAutomate () : 
def genererAutomate (array, porte):
    global passwordArray 
    global porteArray
    
    #validPasswords.clear()
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
        if len(currentLineArray) == 2 :
            tempArray.append(currentLineArray[0])
            tempArray.append(currentLineArray[1])
        elif currentLineArray == 1 :
            tempArray.append("")
            tempArray.append(currentLineArray[0])
    for current in tempArray: #separe les mots de passes et les portes
        print
        if "Porte" in current:
            porteArray.append(current)
        else:
            passwordArray.append(current)
    tempArray.clear()
    global validPasswords
    validPasswords.clear()
    validPasswords.append("")
    return

#def checkPassword(porte):
#    passwordFound = False
#    for current in validPasswords:
#        if current == passwordArray[porteArray.index(porte)]:
#            passwordFound = True
#            break
#    return passwordFound

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
            ouvrirPorte("Porte1.txt", "Porte1")
            labyritheEntrer = True
            current = "m"
        elif current == "b":
            if labyritheEntrer:
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
