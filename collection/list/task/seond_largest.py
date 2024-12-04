arr=[2,3,5,7,10,24]

greatest=0

for i in arr:

    if i>greatest:

        greatest=i

arr=[x for x in arr if x!=greatest]

sgreatest=0

for i in arr:

    if i>sgreatest:

        sgreatest=i

print(sgreatest)