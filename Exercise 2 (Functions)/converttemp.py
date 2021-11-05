def convert_temp(): #defining the function
    tf = eval(input("Enter a temperature in Fahrenheit : ")) #input the original temperature in Fahrenheit
    tc = (5/9)*(tf-32) #conversion formula from Fahrenheit to Celcius
    tk = tc + 273.15 #conversion formula from Celcius to Kelvin
    print(f"The temperature in Fahrenheit is : {tf}") 
    print(f"The temperature in Celcius is : {tc}")
    print(f"The temperature in Kelvin is : {tk}")

convert_temp()