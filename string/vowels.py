text="hElloworld".casefold()

for ch in text:

    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':

        print(ch,end='\t')

#OR

vowels=['a','e','i','o','u']

for ch in text:

    if ch in vowels:

        print(ch,end="\t")