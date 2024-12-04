f=open("D:\\python\\luminar\\datasets\\test\\TEST13.txt")

for line in f:

    if line!="\n":
        print(line.rstrip("\n"))