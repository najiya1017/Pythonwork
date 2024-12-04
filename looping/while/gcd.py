num1=int(input("num1:"))

num2=int(input("num2:"))

i=1

while(i<=num1 and i<=num2):

    if(num1%i==0 and num2%2==0):

        gcd=i

    i=i+1

print("GCD:",gcd)