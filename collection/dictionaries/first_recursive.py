text="ABBCAB"

character_count={}

for ch in text:

    if ch in character_count:

        print(ch)

        break

    else:

        character_count[ch]=1