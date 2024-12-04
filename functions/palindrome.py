def is_palindrome(number):

    original=number

    reverse=0

    while number!=0:

        digit=number%10

        reverse=reverse*10+digit

        number=number//10

    return True if reverse==original else False


print("IS  111 PALINDROME:",is_palindrome(111))