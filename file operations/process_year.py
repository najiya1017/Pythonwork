f=open("D:\\python\\luminar\\datasets\\years.txt")

f_cent=open("D:\\python\\luminar\\datasets\\century.txt","w")

f_leap=open("D:\\python\\luminar\\datasets\\leap.txt","w")

def is_century(year):

    return True if year%100==00 else False

def is_leap_year(year):

   if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

     return True 
    
   else:

        return False

for year in f:

    year=int(year)

    if is_century(year):

        f_cent.write(str(year)+"\n")

    if is_leap_year(year):

        f_leap.write(str(year)+"\n")


f.close()

f_cent.close()

f_leap.close()