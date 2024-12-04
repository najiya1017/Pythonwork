f=open("D:\\python\\luminar\\datasets\\fruits.txt")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)