import math
side = float(input("Enter the side length of the hexagon:"))

area = (3*math.sqrt(3)/2)*(math.pow(side,2))

print(f"The area of a hexagon with side length {side} is {format('%.3f' % area)}.")
