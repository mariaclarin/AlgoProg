import re
import os 

file = os.chdir ("C:/Users/clari/Documents/GitHub/AlgoProg/Exercise 3 (Files)/")
file = open("textfile.txt")
text = file.read() #reading the file
sentences= re.split(r'(?<=[^A-Z].[.?!]) +(?=[A-Z])', text)  #using regex to split the sentences in the file according to the boundaries
for i in sentences: #prints the sentences as newlines each
    print(i)

