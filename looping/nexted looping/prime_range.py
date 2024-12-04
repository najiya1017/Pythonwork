start=int(input("START:"))

end=int(input("END:"))

for i in range(start,end+1):

    is_prime=True

    for num in range(2,i):

        if i%num==0:

            is_prime=False

            break

    if is_prime==True:

        print(i)