#program to find the average word length
from string import punctuation

path =r"C:\Users\RiDiBuAr\PycharmProjects\ForumFileExercise\rosebushexercpt.txt"

file = open(path, "r")

spliText = file.read() #gets the text as a string

cleanText = spliText.translate(str.maketrans('', '', punctuation)) #removes punctuation from the text

spacelessText = cleanText.replace(" ", "") #removes spaces from the text as spaces increase the lentgh of the text
textLength = len(spacelessText)

myList = cleanText.split() #every individual word is stored into a list
listLength = len(myList)

avrgLen = textLength / listLength

print(avrgLen)