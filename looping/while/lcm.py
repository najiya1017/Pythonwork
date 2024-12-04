num1=int(input("Num1:")) 

num2=int(input("Num2:")) 

found=False

i=1

while(found==False): 

    val=num1*i 

    if (val%num2==0): 

        found=True 

    else :

        i+=1

print(val)


