def is_armstrong(number):

    leng=len(str(number))

    total=0

    original=number

    while number!=0:

        digit=number%10

        s_digit=digit**leng

        total+=s_digit

        number=number//10

    print("ARMSTRONG" if total==original else "NOT ARMSTRONG")

is_armstrong(9)