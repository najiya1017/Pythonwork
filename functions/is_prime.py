# is_prime(num)

def is_prime(num):

    is_prime=True

    for i in range (2,num):

        if num%i==0:

            is_prime=False

            break

    print("Prime" if is_prime==True else "Not prime")

num=int(input("Number:"))

is_prime(num)