from re import finditer

text="I have 3 cars,2 bike,1 Cycle"

# pattern="\w" 

# pattern="\d"

# pattern="\D"

# pattern="\W"

# pattern="\s"

pattern="\S"

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())