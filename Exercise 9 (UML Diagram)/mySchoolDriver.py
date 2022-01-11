from mySchool import *

def main():
    new = Person("Dwayne", "The Rock")
    print(Person.__str__(new))
    print()

    reAddress = input("Would you like to update address? (Yes/No) : ")
    if reAddress == "Yes":
        newAddress = input("Enter new address : ")
        new.setAddress(newAddress)
        print()
        print("Here is the updated data :")
        print(Person.__str__(new))
        print()
    elif reAddress == "No" :
        pass

    confirmation = input("Please classify as a student or a teacher! (S/T) : ")
    if confirmation == "S":
        print("Here is the updated data :")
        print(Student.__str__(new))
    elif confirmation == "T":
        print("Here is the updated data :")
        print(Teacher.__str__(new))

main()