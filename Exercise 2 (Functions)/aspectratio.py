import math #used to enable the gcd function

def calc_new_height(): #defining the function
    width = eval(input("Enter the current width : ")) #input of the original width 
    height = eval(input("Enter the current height : ")) #input of the original height
    new_width = eval(input("Enter the desired width : ")) #input of the desired width, to find the ratio
    gcd = math.gcd(width,height) #finding the original aspect ratio
    x = width/gcd #aspect ratio of the width
    y = height/gcd #aspect ratio of the height
    new_height = (new_width/x)*y #formula of finding the new height with the aspect ratio

    print(f"The corresponding height is : {new_height}")

calc_new_height()