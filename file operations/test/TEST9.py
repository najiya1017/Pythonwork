f=open("D:\\python\\luminar\\datasets\\test\\TEST5.txt")

line_number=1

for line in f:

    if line_number%2==0:

        print(line.rstrip("\n"))

    line_number+=1