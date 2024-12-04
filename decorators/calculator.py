def swap_dec(fn):

    def wrapper(n1,n2):

        if n1<n2:

            (n1,n2)=(n2,n1)

        return fn(n1,n2)

    return wrapper

def round_dec(fn):

    def wrapper(n1,n2):

        n1=round(n1)

        n2=round(n2)

        return fn(n1,n2)

    return wrapper

@round_dec
@swap_dec
def addition(num1,num2):

    return num1+num2

@round_dec
@swap_dec
def substraction(num1,num2):

    return num1-num2

@round_dec
@swap_dec
def division(num1,num2):

    return num1/num2

print(addition(10,23.4))

print(substraction(10,23.4))

print(division(10,23.4))



