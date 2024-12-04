arr=[1,3,5,6,2,3,6]

arr.sort()

duplicate=[]

for i in range(0,len(arr)-1):

    j=i+1

    if arr[j]-arr[i]==0 and arr[i] not in duplicate:

        duplicate.append(arr[i])

print(duplicate)