def factorial(number):

    fact=1

    for i in range(2,number+1):

        fact=fact*i  

    return fact if number>0 else -fact

def test_factorial():

    assert factorial(6)==720,"fact calculation test failed"

    assert factorial(-6)==-720,"-ve fact calculation test failed"

try:

    test_factorial()

    print("test passed")

except Exception as e:

    print(e)