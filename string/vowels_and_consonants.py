text="pneumonoultramicroscopicsilicovolcanoconiosis".casefold()

count_vowels=0

count_consonants=0

vowel_sequence=('a','e','i','o','u')

for ch in text:

    if ch in vowel_sequence :

        count_vowels=count_vowels+1

    else:

        count_consonants=count_consonants+1


print("vowels:",count_vowels)

print("consonants:",count_consonants)