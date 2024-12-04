number=int(input("number:"))

original=number

length=len(str(number))

sum=0

for i in range(1,10):

    digit=number%10

    sdigit=digit**length

    sum=sum+sdigit

    number=number//10

    if number==0:

        break

print("Armstrong" if sum==original else "Not Armstrong")