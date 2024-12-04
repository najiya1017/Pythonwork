text="ABBCABCDDABBACGH"

character_count={}

for ch in text:

    if ch in character_count:

        character_count[ch]+=1

    else:

        character_count[ch]=1

print(character_count)

#or

character_count={ch:text.count(ch) for ch in text}

print(character_count)

#print non recursive elements.

non_recursive={ch:text.count(ch) for ch in text if text.count(ch)==1}

for i in non_recursive.keys():

    print(i)

#OR

for k,v in character_count.items():

    if v==1:

        print(k)

#OR

non_recursive_count=[k for k,v in character_count.items() if v==1]

print(non_recursive_count)

print("=================")

#most recursive character

print("MAX:",max(text,key=lambda ch : text.count(ch)))

#least recursive character

print("MIN:",min(text,key=lambda ch : text.count(ch)))
