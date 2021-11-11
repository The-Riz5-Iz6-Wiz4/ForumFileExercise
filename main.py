#importing regular expressions

import re

#program to split sentences based on sentence boundaries

path =r"C:\Users\RiDiBuAr\PycharmProjects\ForumFileExercise\miyagi.txt"

file = open(path, "r")

fileStr = file.read()

#Using re.sub to create new lines based on a pattern
#the code directly below this checks for titles followed by a period
#and then followed by a capital letter from A to Z. If it does not fulfill ALL those requirements
#a new line is created
newStr = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)(?<!Jr)\.\s([A-Z])', r'.\n\1', fileStr)

#the next two lines of code will simply check for ! and ? respectively and adds
#a new line if there is either

newStr2 = re.sub(r'!\s', '!\n', newStr)
newStr3 = re.sub(r'\?\s', '!\n', newStr2)

#this final line checks for any ellipsis and makes a new line should there be one
newStr4 = newStr3.replace("... ", "...\n")

print(newStr4)

