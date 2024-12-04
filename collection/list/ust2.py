arr=[100,200,300,400,500,600,700,800,900]#9

left=1

right=len(arr)-1 if len(arr)%2==0 else len(arr)-2

while (left<right):

    arr[left],arr[right]=arr[right],arr[left]

    left+=2

    right-=2

print(arr)