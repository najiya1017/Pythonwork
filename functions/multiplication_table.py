def multiplication_table(number,n=10): #setting 10 as default value for n

    for i in range(1,n+1):

        print(f"{number}*{i}={number*i}")

# no=int(input("Multiplication table of :"))

# till=int(input("Till:"))

multiplication_table(100)