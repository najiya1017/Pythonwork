num1=int(input("Num1:"))

num2=int(input("Num2:"))

# end=num2 if num2<num1 else num1 #OR end=min(num1,num2)

# for i in range(1,end+1):

#     if num1%i==0 and num2%i==0:

#         hcf=i

# lcm=(num1*num2)//hcf

max=max(num1,num2)

end=num1*num2

for i in range(max,end+1,max):

    if i%num1==0 and i %num2==0:

        print(i)

        break

        

#lcm

#gcd

#armstrong

#prime

#leap year





    