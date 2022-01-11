class ShopListMC :
    def __init__(self, name, amount) :   # initializer method with two parameters accepted
        self.__nameMC = name             # the 4 requested hidden attributes; name of the food
        self.__amountMC = amount         # amount of each food 
        self.__StandardPriceMC = self.getStandardPriceMC() # standard price of food item per pound
        self.__CalculatedPriceMC = self.getCalculatedPriceMC() # calculated price of the ordered item
    
    def __PriceListMC(self):             # a private method that stores the list of items and price per pound. 
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

    def getCalculatedPriceMC(self): # a function to get the calculated price of the food according to the amount ordered.
        self.__CalculatedPriceMC = self.__amountMC * self.getStandardPriceMC()
        return self.__CalculatedPriceMC

    def getStandardPriceMC (self):  # a function to access the standard price for each food in the pricelist. 
        self.__PriceListMC()
        return self.__StandardPriceMC

    def getNameMC(self) :           # a getter method to get the name of each food.
        return self.__nameMC 

    def getAmountMC(self) :         # a getter method to get the amount of food ordered for each food.
        return self.__amountMC 
    

