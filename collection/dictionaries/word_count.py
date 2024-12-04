text="this is a simple program this program count the word count this program is simple "

words=text.split(" ")

word_count={}

for w in words:

    if w in word_count:

        word_count[w]+=1

    else:

        word_count[w]=1

print(word_count)

#OR

word_counts={word:words.count(word) for word in words }

print(word_counts)

#print recursive words

recursive_words=[k for k,v in word_counts.items() if v>1]

print(recursive_words)

#display non-recursive words

non_recursive=[k for k,v in word_counts.items() if v==1]

print(non_recursive)

#most recursive word

print(max(recursive_words,key=lambda word:word_counts.get(word)))