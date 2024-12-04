f=open('D:\\python\\luminar\\datasets\\test\\TEST5.txt')

search="program"

for line in f:

    if search in line:

        line=line.replace(search,"hello")

    print(line.rstrip("\n"))

