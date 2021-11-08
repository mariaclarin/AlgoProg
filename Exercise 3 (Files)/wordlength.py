import os 
import re

os.chdir("C:/Users/clari/Documents/GitHub/AlgoProg/Exercise 3 (Files)/")
file = open("ebook.txt", "r")

all = re.findall('\w+', file.read().lower())

wordlength = []
for word in all :
    wordlength.append(len(word))
    total = sum(wordlength)
    average = total/len(all)

print(average)

