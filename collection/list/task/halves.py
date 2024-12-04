lst1=[2,4,5,6,3,6,]

length=len(lst1)

new1=[]

new2=[]

for i in range(0,length//2):

    new1.append(lst1[i])

print(new1)

for i in range(length//2,length):

    new2.append(lst1[i])

print(new2)

