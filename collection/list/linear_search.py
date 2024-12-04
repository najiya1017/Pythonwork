arr=[2,4,5,6,67]

search_element=int(input("Enter Search Element:"))

found=False

for i in range(0,len(arr)):

    if arr[i]==search_element:

        found=True

        break

print(found)