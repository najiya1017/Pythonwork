arr=[1,2,5,6]

arr.sort()

for i in range(0,len(arr)-1):

    j=i+1

    if arr[j]-arr[i]!=1:

        print(arr[i]+1)

      