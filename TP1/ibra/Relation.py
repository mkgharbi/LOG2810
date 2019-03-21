class Relations: 
    def __init__(self, nomIndividu1 , nomIndividu2, facteurRelations):
        self.__nomIndividu1 = nomIndividu1
        self.__nomIndividu2 = nomIndividu2
        self.__facteurRelations = facteurRelations
    
    def getNomIndividu1(self):
        return self.__nomIndividu1
    def getNomIndividu2(self):
        return self.__nomIndividu2
    def getFacteurRelations(self):
        return self.__facteurRelations

    def setNomIndividu1(self, nomIndividu1):# est ce le paramettre va se melanger avec celui du par constructeur
        self.__nomIndividu1 = nomIndividu1
    def setNomIndividu2(self,nomIndividu2):
        self.__nomIndividu2 = nomIndividu2
    def setFacteurRelation(self,facteurRelations):
        self.__facteurRelations = facteurRelations 
