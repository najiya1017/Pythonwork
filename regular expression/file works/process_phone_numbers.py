from re import fullmatch

f=open("D:\\python\\luminar\\datasets\\dataset regular expression\\phone_numbers.txt")

for line in f:

    phone=line.rstrip("\n")

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    if matcher!=None:

        print(phone)