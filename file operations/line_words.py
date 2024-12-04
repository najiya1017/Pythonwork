f=open("D:\\python\\luminar\\datasets\\words2.txt")

words=[]

for line in f:

    line=line.rstrip("\n")

    all_words=line.split(" ")

    words.extend(all_words)

word_count={w:words.count(w) for w in words}

value_key=[[v,k] for k,v in word_count.items()]

# max_word=max(words,key=lambda w: words.count(w))

print(word_count)

print(sorted(value_key,reverse=True))

# print(max_word)