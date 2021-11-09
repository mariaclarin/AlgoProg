# import os 
import re

# os.chdir("C:/Users/clari/Documents/GitHub/AlgoProg/Exercise 3 (Files)/")
file = open("ebook.txt", "r")
all = re.findall('\w+', file.read()) #finding all words in the file 
average = sum([len(word) for word in all]) / len(all) #average formula, length of each word divided by the number of words found in the file

print("The average word length in this file is :", average)

