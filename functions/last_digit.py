# print number which has the last digit which is greater
 
def last_digit(num1,num2):

    last_digit1=num1%10

    last_digit2=num2%10

    print(num1 if last_digit1>last_digit2 else num2)

last_digit(123,872)