expenses=[12000,13000,14000,11000,13000,2,2,2,2,2]

count=0

for i in expenses:

    rcount=expenses.count(i)

    if rcount>count:

        count=rcount

        num=i

print(num)

