def add_numbers(*args):

    total=0

    for num in args:

        total+=num

    print(total)

add_numbers(10,20)

add_numbers(10,20,30)


def second_largest(*args):

   sorted_numbers=sorted(args,reverse=True)

   return sorted_numbers[1]


print(second_largest(10,20,30))

print(second_largest(10,20,30,9,70,29,50,100))