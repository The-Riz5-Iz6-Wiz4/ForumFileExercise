#program for numbering lines in a text from 1 to n

path =r"C:\Users\RiDiBuAr\PycharmProjects\ForumFileExercise\random.txt"

file = open(path, "r")
newFile = open('numbered.txt', 'w') #creates new file in the same directory if (insertname).txt does not exist

spliText = file.read().split("\n") #creates a list for every line

num = 0

while num < len(spliText):
    spliText[num] = str(num) + "." + spliText[num] + "\n" #str(num) converts an int into a str
                                                          #spliText[num] gets the variable from the list corresponding to num
    newFile.write(spliText[num]) #writes to the file
    num += 1

file.close()
newFile.close()

#important note.
#Obtaining txt files from the web or copying words from the web
#to a text file directly can result in extra letters/words appearing
#I think it's because of different file format?