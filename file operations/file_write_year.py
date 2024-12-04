f=open("D:\\python\\luminar\\datasets\\years.txt","w")

for year in range(1800,2025):

    f.write(str(year)+"\n")

f.close()