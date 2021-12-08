import os 
def hapax(all) : #defining a word counter function
    words = all.split() #splitting lines/sentences into words
    for word in words :
        if word in count :
            count[word] += 1
        else : 
            count[word] = 1
    return count

os.chdir("C:/Users/clari/Documents/GitHub/AlgoProg/Exercise 3 (Files)/")
file = open("ebook.txt", "r") #opening the file in the directory, declaring that it will only be read.
all = file.read().lower() #reading the file and making sure all words inputed will be in lowercase
words_compilation = "" #a storage variable to store all the words when filtering puctuations.

count = dict() 
count = hapax(all)

for i in count :
    if count[i] == 1 : #if the appearance count of the word is equal to 1, it will continue the print function below.
        print(i,",", end="")

file.close() #closing the file

