def is_perfect (number):

    total=0

    for i in range(1,number):

        if number%i==0:

            total+=i

    print("PERFECT NUMBER" if total==number else "NOT PERFECT NUMBER")


is_perfect(400)
