num1=int(input("num1:"))

num2=int(input("num2:"))

num3=int(input("num3:"))

if (num1>=num2 and num1>=num3): 

    if num2>num3:

        print("num2 is second largest")
    
    else:

        print("num3 is second largest")

elif (num2>=num1 and num2>=num3):

    if num1>num3:
        
        print("num1 is second largest")
    
    else:

        print("num3 is second largest")


elif (num3>=num1 and num3>=num2):

    if num1>num2:
        
        print("num1 is second largest")
    
    else:

        print("num2 is second largest")


elif num1==num3 and num1==num2 :

    print("Three numbers are same")
