prev=0

print(prev)

for row in range(2,8):

    prev=0

    current=1

    print(prev,end="\t")

    print(current,end="\t")

    for col in range(3,row+1):

        next=prev+current

        print(next,end="\t")

        prev=current

        current=next

    print()







