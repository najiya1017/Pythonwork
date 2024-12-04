text1="ABCDEFR"

text2="PQRSTYU"

#output=APBQCRDS
for i in range(0,max(len(text1),len(text2))):

    if i<len(text1):

        print(text1[i],end='')

    if i<len(text2) :

        print(text2[i],end='')


    