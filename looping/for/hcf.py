num1=int(input("Num1:"))

num2=int(input("Num2:"))

end=num2 if num2<num1 else num1 #OR end=min(num1,num2)

for i in range(1,end+1):

    if num1%i==0 and num2%i==0:

        hcf=i

print(hcf)



    