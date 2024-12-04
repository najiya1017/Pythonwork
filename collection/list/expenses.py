expenses=[12000,13000,14000,11000,13000,78000]

#TO PRINT EACH VALUE IN LIST
# for i in expenses:

#     print(i)

#TO FIND THE TOTAL SUM
# total=0

# for i in expenses:

#     total+=i

# print(total)

#TO FIND MAXIMUM EXPENSES
maxi=expenses[0]

mini=expenses[0]

for i in expenses: #i takes each value in the list not index

    maxi=i if i>maxi else maxi

    mini=i if mini>i else mini

print(f"MAX:{maxi} , MIN:{mini}")


