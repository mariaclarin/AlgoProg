a = float(input("Enter length of edge1 : "))
b = float(input("Enter length of edge2 : "))
c = float(input("Enter length of edge3 : "))
perimeter = a + b + c

if a+b>=c and a+c>=b and b+c>=a :
    print (f"The perimeter is {perimeter}.")
else :
    print("Perimeter cannot be calculated: the input is invalid.")