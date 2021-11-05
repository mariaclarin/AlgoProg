import math
mass = float(input("Enter the mass of the cart (in kg): "))
force = float(input("Enter the force to push the cart (in N): "))
g = 9.8

angle = math.sinh(force/(mass*g))
degree = math.degrees(angle)

print(f"The angle of the ramp is {format('{degree} = %.1f' % degree)} degrees.")