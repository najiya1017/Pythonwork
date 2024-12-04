arr=[1,2,3,2,1,5,3,2,4,5,5]

final=[]

for num in arr:

    if num not in final:

        final.append(num)

print(final)