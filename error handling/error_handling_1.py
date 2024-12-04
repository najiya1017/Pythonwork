num1=int(input("NUM1:"))

num2=int(input("NUM2:"))

try:

    result=num1/num2

    print(result)

except Exception as e: #Exception as e==>to show what error occured

    print(e)

    num2=int(input("Enter number other than zero:"))

    result=num1/num2

    print(result)

finally:

    print("file transfer")

    print("database commit")