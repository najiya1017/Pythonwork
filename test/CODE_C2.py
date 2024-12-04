def next_prime(number):

    number=number+1

    while True:

        is_prime=True

        for i in range(2,number):

            if number%i==0:

                is_prime=False

                break

        if is_prime==True:

            break

        number+=1

    print(number)

next_prime(7)

next_prime(14)