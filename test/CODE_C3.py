def longest_word(text):

    words=text.split(" ")

    longest_word=max(words,key=lambda w:len(w))

    print(longest_word)

text = "Hello world! This is a test for finding the longest word"

longest_word(text)
