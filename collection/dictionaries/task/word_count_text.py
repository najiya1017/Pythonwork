text="this is a simple program this program count the word count this program is simple"

words=text.split(" ")

word_count={num:words.count(num) for num in words}

print(word_count)
