from shoplistMC import ShopListMC #importing the class from my class file.

def orderingMC() :  # function to input the order
    items = []      # an empty list
    OrderAmount = int(input("How many items will you order today? "))           #inputs the number of items for the loop.
    while OrderAmount <1:                                                       
        print("Number of items must be at least 1.")                            #validation check for number of items.
        OrderAmount = eval(input("How many items will you order today? "))      #reinput if the previous input doesn't pass the validation check.

    for i in range (OrderAmount) :                                              #loops for the amount of items as inputed previously.
        print(f"Item#{i+1}-")                                                   #item numbering.
        name =str(input('Enter food: '))                                        #inputing food name as one item.
        amount = float(input("Enter amount of pounds : "))                      #inputing amount of pounds per item.
        while amount <= 0:
            print("Amount of pounds must be greater than 0. ")                  #validation check for the amount of pounds per item.
            amount = float(input("Enter amount of pounds : "))                  #reinput if the previous input doesn't pass the validation check.
        print()                                                                 #adding a new line
        item = ShopListMC(name, amount)                                         
        items.append(item)                                                      #adding each item to the list
    return items

def ReceiptDisplayMC(orderlist) :
    print("Here's a summary of the items purchased:")
    print("----------------------------------------")
    for item in orderlist:                                                      #loop printing each item's data (name, amount, price, calculated price) with proper formatting
        print(f"Item : {item.getNameMC()} ")
        print("Amount ordered : {:.1f}".format(item.getAmountMC()))
        print("Price per pound : ${:.2f}".format(item.getStandardPriceMC()))
        print("Price of order : ${:.2f}".format(item.getCalculatedPriceMC()))
        print()                                                                 #adding a new line

def TotalCosttMC(orderlist):                                
    total = 0
    for item in range(len(orderlist)):
        total= total + orderlist[item].getCalculatedPriceMC()                   #formula for the total cost. Will add the calculated price of each item to the total.
    print("Total cost: ${:.2f}".format(total))                                 #printing the total cost in proper formatting

def main():                 #defining a main() function to call 3 previous functions.
    items = orderingMC()
    ReceiptDisplayMC(items)
    TotalCosttMC(items)

main()  #calling the main function