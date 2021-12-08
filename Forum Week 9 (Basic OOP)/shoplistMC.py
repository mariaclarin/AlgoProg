class ShopListMC :
    def __init__(self, name, amount) :
        self.__nameMC = name
        self.__amountMC = amount
        self.__StandardPriceMC = self.getStandardPriceMC()
        self.__CalculatedPriceMC = self.getCalculatedPriceMC()
    
    def __PriceListMC(self):
        if self.__nameMC == "Dry Cured Iberian Ham":
            self.__StandardPriceMC = 177.80
        elif self.__nameMC == "Wagyu Steaks":
            self.__StandardPriceMC = 450.00
        elif self.__nameMC == "Matsutake Mushrooms":
            self.__StandardPriceMC = 272.00
        elif self.__nameMC == "Kopi Luwak Coffee":
            self.__StandardPriceMC = 306.50
        elif self.__nameMC == "Moose Cheese":
            self.__StandardPriceMC = 487.20 
        elif self.__nameMC == "White Truffles":
            self.__StandardPriceMC = 3600.00
        elif self.__nameMC == "Blue Fin Tuna" :
            self.__StandardPriceMC = 3603.00  
        elif self.__nameMC == "Le Bonnotte Potatoes":
            self.__StandardPriceMC = 270.81
        else:
            self.__StandardPriceMC = 0.00

    def getCalculatedPriceMC(self):
        self.__CalculatedPriceMC = self.__amountMC * self.getStandardPriceMC()
        return self.__CalculatedPriceMC
        
    def getStandardPriceMC (self):
        self.__PriceListMC()
        return self.__StandardPriceMC

    def getNameMC(self) :
        return self.__nameMC 

    def getAmountMC(self) :
        return self.__amountMC 
    

