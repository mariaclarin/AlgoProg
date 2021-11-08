import os 
import string
def hapax(all) :
    words = all.split()
    for word in words :
        if word in count :
            count[word] += 1
        else : 
            count[word] = 1
    return count

os.chdir("C:/Users/clari/Documents/GitHub/AlgoProg/Exercise 3 (Files)/")
file = open("ebook.txt", "r")
all = file.read().lower()
words_compilation = ""

for word in all :
    if word not in string.punctuation :
        words_compilation += word
all = words_compilation

count = dict()
count = hapax(all)

for i in count :
    if count[i] == 1 :
        print(i,",", end="")

file.close()

