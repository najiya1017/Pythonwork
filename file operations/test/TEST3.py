f=open("D:\\python\\luminar\\datasets\\test\\TEST3.txt")

word=[]

for line in f:

    line=line.rstrip("\n")

    all_words=line.split(" ")

    word.extend(all_words)

# print(word)

word_count={w:word.count(w) for w in word}

print(word_count)