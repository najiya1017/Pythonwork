text1="arc"

text2="car"

is_anagram=True

for ch in text1:

    if ch not in text2:

        is_anagram=False

print(is_anagram)