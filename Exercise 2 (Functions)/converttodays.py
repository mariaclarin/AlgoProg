def convert_to_days() :  #defining the function
    hrs = float(input("Enter number of hours : ")) #input the amount of hours to be converted to days
    min = float(input("Enter number of minutes : ")) #input the amount of minutes to be converted to days
    sec = float(input("Enter number of seconds : ")) #input the amount of seconds to be converted to days
    hrs_day = hrs/24 #hours - days conversion formula
    min_day = min/1440 #minutes - days conversion formula
    sec_day = sec/86400 #seconds - days conversion formula
    day = hrs_day + min_day + sec_day #total of days formula
    print("The number of days is : " '{:.4f}'.format(day)) #printing the final answer to 4 decimal points

convert_to_days()
    