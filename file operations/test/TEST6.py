f=open("D:\\python\\luminar\\datasets\\test\\TEST3.txt")

words=[]

for line in f:

    line=line.rstrip("\n")

    word=line.split(" ")

    words.extend(word)

max_word=max(words,key=lambda w:len(w))

print(max_word)