def factorial(num):

    product=1

    for i in range(1,num+1):

        product=product*i

    # print(product)

    return product

num=int(input("Number:"))

result=factorial(num)

print(result)