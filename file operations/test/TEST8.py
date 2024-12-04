f=open("D:\\python\\luminar\\datasets\\test\\TEST5.txt")

count_word="program"

words=[]

for line in f:

    line=line.rstrip("\n")

    word=line.split(" ")

    words.extend(word)

print(words.count(count_word))