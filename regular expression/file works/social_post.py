from re import finditer

f=open("D:\\python\\luminar\\datasets\\dataset regular expression\\social_post.txt")

for line in f:

    line=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,line)

    for obj in matcher:

        print(obj.group())