text="this is a simple programing question to find word with maximum number of characters"

words=text.split(" ")

#to return word with maximum length 

# print(max(words,key=lambda w :len(w)))
print(max(words,key=len))

#to return sorted array based on length in descending order

srt_array=sorted(words,key=lambda w:len(w),reverse=True)

print(srt_array)

#most recursive character

# recursive_character=max(words,key=lambda w : words.count(w))
recursive_character=max(words,key=words.count)
print(recursive_character)