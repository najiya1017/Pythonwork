num1=int(input("Number 1:"))

num2=int(input("Number 2:"))

max=max(num1,num2)

for i in range(max,(num1*num2)+1,max):

    if i%num1==0 and i%num2==0:

        print("lcm=",i)

        break