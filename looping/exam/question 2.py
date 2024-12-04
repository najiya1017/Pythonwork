number=int(input("Number:"))

is_prime=True

for i in range(2,number):

    if number%i==0:

        is_prime=False

        break

print("PRIME" if is_prime==True else "NOT PRIME")

len=len(str(number))

original=number

sum=0

while (number!=0):

    digit=number%10

    sdigit=digit**len

    sum=sum+sdigit

    number=number//10

print("ARMSTRONG" if sum==original else "NOT ARMSTRONG" )