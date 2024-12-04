from re import finditer

text="ababbabbaaaab"

# pattern="a{3}"

# pattern="a{1,3}"
pattern="a{3}"

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())