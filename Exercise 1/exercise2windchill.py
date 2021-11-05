temp = float(input("Enter the temperature in Fahrenheit: "))

while True :
    if temp < -58 or temp > 41 :
        print("Temperature must be between -58F and 41F.")
        temp = float(input("Please re-enter the temperature in Fahrenheit: "))
    else :
        break



speed = float(input("Enter the wind speed miles per hour: "))

while True :
    if speed < 2 :
        print("Speed must be greater than or equal to 2.")
        speed = float(input("Please re-enter the wind speed miles per hour: "))
    else :
        break


windchill = 35.74 + (0.6215*temp) - (35.75*(speed**0.16)) + (0.4275*temp*(speed**0.16))
print(f"The wind chill index is {format('{windchill} = %.3f' % windchill)}.")