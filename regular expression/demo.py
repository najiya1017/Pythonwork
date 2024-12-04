from re import finditer

text="ababbbaaab"

pattern="ab"

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())

text2="fatcatrunsfasttocattherat"

matcher2=finditer("at",text2)

for obj in matcher2:

    print(obj.start(),obj.group())

