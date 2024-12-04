num=int(input("number:"))
total=0
for i in range(1,num):

    if num%10==0:

        total+i

print("perfect number" if total==num else "not perfect")
