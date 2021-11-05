purchase = float(input("Enter the number of packages purchased: "))

if purchase < 10 :
    disc = 0
elif 10 <= purchase < 20 :
    disc = 10
elif 20 <= purchase < 50 :
    disc = 20
elif 50 <= purchase < 100 :
    disc = 30
elif purchase >= 100 :
    disc = 40

pack = purchase*99
disctotal = (disc/100)*pack
total = pack - disctotal
print("Discount Amount @ ", disc,"% : ${:.2f}".format(disctotal))
print("Total amount : ${:.2f}".format(total))
