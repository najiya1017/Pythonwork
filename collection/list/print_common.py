arr1=[10,13,8,11,20]  #[8, 10, 11, 13, 20]

arr2=[2,20,8,7]  #[2, 7, 8, 20]

arr1.sort()

arr2.sort()

p1=0

p2=0

while (p1<len(arr1) and p2<len(arr2)):

    if arr1[p1]==arr2[p2]:

        print(arr1[p1])

        p1=p1+1

        p2=p2+1

    elif arr1[p1]>arr2[p2]:

        p2=p2+1

    elif arr2[p2]>arr1[p1]:

        p1=p1+1






