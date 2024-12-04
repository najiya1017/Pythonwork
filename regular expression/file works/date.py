from re import findall

f=open("D:\\LUMINAR\\python\\luminar\\datasets\\dataset regular expression\\data.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

date=findall(pattern,content)

for obj in date:

    print(obj)