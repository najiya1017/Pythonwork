# text="BCDAGHD"

# found=False

# for i in range(0,len(text)):

#     for j in range(i+1,len(text)):

#         if text[i]==text[j]:

#             found=True

#             break

#     if found==True:

#         break

# print(text[i] if found==True else "NO RECURSIVE CHARACTER")



text = "BCDAGHD"
seen = set()  #for faster look up,find a value on set has a complexity odf O(1),bcoz set uses hash to find the value

for char in text:
    if char in seen:
        print(char)
        break
    seen.add(char)
else: #this is for-else,else will block will work if there is no break in the loop.
    print("NO RECURSIVE CHARACTER")