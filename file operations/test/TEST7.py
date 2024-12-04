f=open("D:\\python\\luminar\\datasets\\test\\TEST3.txt")

lines=[]

for line in f:

    line=line.strip("\n")

    lines.append(line)

reverse_line=lines[::-1]

for line in reverse_line:

    print(line)