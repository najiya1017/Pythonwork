f=open("D:\\python\\luminar\\datasets\\test\\TEST2.txt","a")

frameworks=["springboot","oodo","wordpress"]

for fw in frameworks:

    f.write(fw+"\n")

f.close()

f=open("D:\\python\\luminar\\datasets\\test\\TEST2.txt")

for fw in f:

    print(fw)

f.close()