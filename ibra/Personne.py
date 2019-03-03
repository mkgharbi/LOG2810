########################


#Classe :
class Personne:

    def __init__(self, nom, couleurDeCheveux, couleurDesYeux, genie):
        self.__nom= nom
        self.__couleurDeCheveux = couleurDeCheveux
        self.__couleurDesYeux = couleurDesYeux
        self.__genie = genie
    def __str__(self):
        return 


    def getNom(self):
        return self.__nom
    def getCouleurDeCheveux(self):
        return self.__couleurDeCheveux
    def getCouleurDesYeux (self):
        return self.__couleurDesYeux
    def getGenie(self):
        return self.__genie

    def setNom(self, nom ):
        self.__nom = nom
    def setCouleurDeCheveux(self,couleurDeCheveux):
        self.__couleurDeCheveux= couleurDeCheveux
    def setCouleurDesYeux(self,couleurDesYeux):
        self.__couleurDesYeux=couleurDesYeux
    def setGenie(self,genie):
        self.__genie= genie

    