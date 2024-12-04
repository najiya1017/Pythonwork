lst1=["apple","mango","onion","potato","pineapple"]

lst2=[100,200,300]

price={}

num=1

for i in range(len(lst1)):

    if i<len(lst2):

        price[lst1[i]]=lst2[i]

    else:

        price[lst1[i]]=num

        num+=1

print(price)

#OR

result={}
num=1
for i in range(0,len(lst2)):
    list_one_index=lst1[i]
    list_two_indexx=lst2[i]

    result[list_one_index]=list_two_indexx

balnced_element=lst1[len(lst2):]
for index,element in enumerate(balnced_element):
    result[element]=index+1

print(result)


    