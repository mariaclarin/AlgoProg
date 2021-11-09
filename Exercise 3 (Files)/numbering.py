import os
os.chdir("C:/Users/clari/Documents/GitHub/AlgoProg/Exercise 3 (Files)/")
file = open("ebook.txt", "r") #opening the file from the directory and declaring it as read only.
output = open("reebook.txt", "w") #creating a new file and allowing the program to write in the file.

count=0
for line in file : #directed to each line in the first input file that we read.
    count+=1 #counts the corresponding line number.
    output.write ("{:2d} {}".format(count,line)) #writing on the new file the line number and the line that represents the line number.

output.close() #closing the file.
