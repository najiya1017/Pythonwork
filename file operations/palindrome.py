f=open("D:\\python\\luminar\\datasets\\words.txt")

f_palindrome=open("D:\\python\\luminar\\datasets\\palindrome.txt","w")

def is_palindrome(word):

    word=word.rstrip("\n")

    reverse=word[::-1]

    return True if reverse==word else False

for word in f:

    if is_palindrome(word):

        f_palindrome.write(word)

f.close()

f_palindrome.close()



