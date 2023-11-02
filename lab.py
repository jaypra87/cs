text = open("text.txt", "r")
myfile = open("myfile.txt", "r")

line = text.read
words = line.split()
for word in words:
    print(word + "\n")
    myfile.write(word)

text.close()
myfile.close()
