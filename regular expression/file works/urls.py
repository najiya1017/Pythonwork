from re import findall

f=open("D:\\python\\luminar\\datasets\\dataset regular expression\\urls.txt")

content=f.read()

pattern=r"https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)