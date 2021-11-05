a = float(input("Enter the subtotal : $"))
b = float(input("Enter tip amount (as a %) : "))

print("Subtotal : ${:,.2f}".format(a))

tip = (b/100)*a 
print("Tip : ${:,.2f}".format(tip))

total = float(a) + float(tip)
print("Total : ${:,.2f}".format(total))