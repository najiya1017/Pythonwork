num1=int(input("number 1:")) 

num2=int(input("number 2:")) 

num3=int(input("number 3:")) 

print()

if num1>=num2 and num1>=num3 :

    print("LARGEST:",num1)

    if num2>=num3:

        print("SECOND LARGEST:",num2)

        print("AFTER SORTING:",num1,num2,num3)

    else:

        print("SECOND LARGEST:",num3)

        print("AFTER SORTING:",num1,num3,num2)

elif num2>=num1 and num2>=num3:

    print("LARGEST:",num2)

    if num1>=num3:

        print("SECOND LARGEST:",num1)

        print("AFTER SORTING:",num2,num1,num3)

    else:

        print("SECOND LARGEST:",num3)

        print("AFTER SORTING:",num2,num3,num1)

elif num3>=num1 and num3>=num2:

    print("LARGEST:",num3)

    if num2>=num1:

        print("SECOND LARGEST:",num2)

        print("AFTER SORTING:",num3,num2,num1)

    else:

        print("SECOND LARGEST:",num1)

        print("AFTER SORTING:",num3,num1,num2)

    