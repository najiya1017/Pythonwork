# number=int(input("Number:"))

# for i in range(1,number+1):

#     if number%i==0:

#         print(i)

num1=int(input("num1:"))

num2=int(input("num2:"))

end=num1 if num1<num2 else num2

for i in range(1,end+1):

    if num1%2==0 and num2%2==0:

        print(i)