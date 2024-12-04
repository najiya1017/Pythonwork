def next_fibonacci_number(number):

    prev=0

    current=1

    next=prev+current

    while next<=number:

        prev,current=current,next

        next=prev+current

    print(next)


next_fibonacci_number(5) 

next_fibonacci_number(13)

