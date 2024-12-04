f=open("D:\\python\\luminar\\datasets\\test\\TEST12.txt")

for line in f:

    line=line.rstrip("\n")

    char_count={line[i]:line.count(line[i]) for i in range(len(line))}

print(char_count)