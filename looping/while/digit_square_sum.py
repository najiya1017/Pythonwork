num=int(input("Enter number:"))

total=0

while(num!=0):

    digit=num%10

    sdigit=digit**2

    total=total+sdigit

    num=num//10

print("sum:",total)