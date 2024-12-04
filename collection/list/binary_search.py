arr=[4,2,64,3,8,10,20]

arr.sort()

search=int(input("Search Element:"))

is_found=False

low=0

upp=len(arr)-1

while(low<=upp):

    mid=(low+upp)//2

    if arr[mid]==search:

        is_found=True

        break

    elif search<arr[mid]:

        upp=mid-1

    elif search>arr[mid]:

        low=mid+1

print(is_found)

