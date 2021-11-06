def nums_atoms(n,w=196.97): #defining the function with n as the amount of an element in grams, and w as the atomic weight 
    formula = (n/w)*(6.022 * (10**23)) #the formula to find the number of atoms
    print(formula) #to print out the answer 

nums_atoms(10, 1.008)