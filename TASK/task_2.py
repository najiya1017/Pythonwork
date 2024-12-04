# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so: wordi: a b word2:
# p q r
# merged: a pbqcr
# Example 2:
# Input: wordl = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end. 
# wordl: a b


# word2:

# p q
# r

# merged: a pb q

# S
# S

word1="abc"
word2="pqr"
minn=min(len(word1),len(word2))
max_word=word1 if len(word1)!=minn else word2
final=""
for i in range(minn):
    final=final+word1[i]+word2[i]

final=final+max_word[minn:]

print(final)
    