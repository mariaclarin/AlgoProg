def calc_weight_on_planet(w,g=23.1): #defining the function with the parameters as w = weight on Earth and optional parameter of g = surface gravity with the default set as 23.1
    m = w/9.8 #formula to find the mass from the weight divided by the gravity on Earth
    print(m*g) #printing out the final answer of the weight in the desired planet

calc_weight_on_planet(120, 23.1)