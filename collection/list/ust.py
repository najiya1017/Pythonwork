arr=[10,20,30,40,50,60]

odd=[arr[i] for i in range(1,len(arr),2)] 

odd.reverse()

j=0

for i in range(1,len(arr),2):

    arr[i]=odd[j]

    j+=1

print(arr)