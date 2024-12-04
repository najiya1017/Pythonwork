source_word="CHICKEN"

target_word="HENN"

count=0

for ch in target_word:

    if ch in source_word and target_word.count(ch)<=source_word.count(ch):

        count+=1

print("kangaroo word" if count==len(target_word) else "not kangaroo word")


#OR

character_count={ch:source_word.count(ch) for ch in source_word}

is_kangaroo=True


for ch in target_word:
   

    if ch in character_count and character_count.get(ch)>0:

        character_count[ch]-=1

    else:

        is_kangaroo=False

        break

print("kangaroo word" if is_kangaroo==True else "not kangaroo word")



