f1=open("D:\\python\\luminar\\datasets\\test\\TEST3.txt")

f2=open("D:\\python\\luminar\\datasets\\test\\TEST10_1.txt")

f_write=open("D:\\python\\luminar\\datasets\\test\\TEST10_2.txt","w")

for line in f1:

    f_write.write(line)

f_write.close()

f_write=open("D:\\python\\luminar\\datasets\\test\\TEST10_2.txt","a")

for line in f2:

    f_write.write(line)

f_write.close()

f1.close()

f2.close()