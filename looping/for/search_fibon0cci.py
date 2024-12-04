number=int(input("Number:"))

prev=0

current=1

found=False

while(found==False):

    next=prev+current
    
    if next>number:

        break

    elif next==number:

        found=True

    prev=current

    current=next

print("PRESENT" if found==True else "NOT PRESENT")

