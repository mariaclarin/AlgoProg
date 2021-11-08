import os
os.chdir("C:/Users/clari/Documents/GitHub/AlgoProg/Exercise 3 (Files)/")
file = open("ebook.txt", "r")
output = open("reebook.txt", "w")

count=0
for line in file :
    count+=1
    output.write ("{:2d} {}".format(count,line))

output.close()
