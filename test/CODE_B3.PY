def print_non_recursive_words(text):

    text=text.casefold()

    words=text.split(" ")

    punctuations=['!','.','?','-']

    words=[word.rstrip(word[len(word)-1]) if word[len(word)-1] in punctuations else word for word in words ]

    non_recursive=[w for w in words if words.count(w)==1]

    print(non_recursive)

print_non_recursive_words("Hello world! This is a test. Hello everyone.")