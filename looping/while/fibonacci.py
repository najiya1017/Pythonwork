end=int(input("Input end number:"))

num1=0

num2=1

print(num1)

print(num2)

count=2

next=num2

while (count<=end):

    print(next)

    num1,num2=num2,next

    next=num1+num2
    
    count=count+1

