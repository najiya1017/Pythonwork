arr=[1,2,5,6]

found=False

integer=1

p1=0

while integer!=arr[len(arr)-1]:

    if arr[p1]!=integer:

        print(integer)

        integer+=1

        found=True

    else:

        p1=p1+1

        integer+=1

if found==False:

    print(len(arr)+1)

