text="this is a test to remove duplicate words this test is simple"

text2="this simple test remove duplicate words"

words=text.split(" ")

words2=text2.split(" ")

print(set(words2).issubset(set(words)))

