text="BCDAGHD"

found=False

for i in range(0,len(text)):

    for j in range(i+1,len(text)):

        if text[i]==text[j]:

            found=True

            break

    if found==True:

        break

print(text[i] if found==True else "NO RECURSIVE CHARACTER")