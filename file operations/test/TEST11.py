f=open("D:\\python\\luminar\\datasets\\test\\TEST11.txt")

lines_count=[]

for line in f:

    line=line.rstrip("\n")

    if line not in lines_count:

        lines_count.append(line)

    else:

        print(line)



