arr=[2,3,4,5,8,9]

# found=False

# for i in range(0,len(arr)-1):

#     for j in range(i+1,len(arr)):

#         if arr[i]+arr[j]==7:

#             found=True

#             num1,num2=arr[i],arr[j]

#             break

#     if found==True:

#             break

# print(num1,num2)


#The above logic isn't good as it increases the complexity.

right=0

left=len(arr)-1

summ=10

while(right<left):

    c_sum=arr[right]+arr[left]

    if c_sum==summ:

        print(arr[right],arr[left])

        break

    elif c_sum<summ:

        right+=1

    else:

        left-=1
