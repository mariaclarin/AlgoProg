import math
a = eval(input("Enter a numerator. Value must be greater than 0: "))
while True :
    if a <= 0 : 
        a = eval(input("Please re-enter the numerator. Value must be greater than 0: "))
    else :
        break

b = eval(input("Enter a denominator. Value must be greater than 0: "))
while True :
    if b <= 0 : 
        b = eval(input("Please re-enter the denominator. Value must be greater than 0: "))
    else :
        break

gcd = math.gcd(a,b) 
x = a//gcd
y = b//gcd

if a < b :
    print(f"{a}/{b} is a proper fraction.")
    if gcd == 1 :
        print("This proper fraction cannot be reduced any further.")
    else :
        print(f"This proper fraction can be reduced to : {x}/{y}.")
elif a >= b :
    print(f"{a}/{b} is an improper fraction.")
    if gcd == 1 :
        print("This improper fraction cannot be reduced any further.")
        if x%y != 0 :
            print(f"The mixed number is {x//y} and {x%y}/{y}.")
        else :
            print(f"The whole number is {x//y}.")
    else : 
        print(f"This improper fraction can be reduced to : {x}/{y}.")
        if x%y != 0 :
            print(f"The mixed number is {x//y} and {x%y}/{y}.")
        else :
            print(f"The whole number is {x//y}.")
