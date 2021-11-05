x1 = float(input("Enter the x-coordinate for point 1: "))
y1 = float(input("Enter the y-coordinate for point 1: "))
x2 = float(input("Enter the x-coordinate for point 2: "))
y2 = float(input("Enter the y-coordinate for point 2: "))

slope = (y2-y1)/(x2-x1)
print(f"The slope for the line that connects two points ({x1} , {y1}) and ({x2} , {y2}) is {format('%.5f' % slope)}.")
