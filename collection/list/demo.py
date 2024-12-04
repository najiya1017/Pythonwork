# define,is duplicate-allowed,insertion order preserved,mutable,methods

#list  can be defined using [] or list()

#duplication is allowed

#insertion order preserved

#mutable means if we can update contents in list,list is mutable

expenses=[12000,13000,14000,11000,13000]
#           0     1     2     3     4

expenses[0]=15000 #changes the value of zeroeth index to the specified value

print(expenses)

#append(self)=method to insert new object to the list at the end

expenses.append(20000)

print(expenses)

#def pop(index)==>remove the last object from list and returns it

popped_element=expenses.pop()

print(expenses)

print(popped_element)

#def insert(index,value to be inseted)==> insert values to list

expenses.insert(0,34000)

print(expenses)

#def sort(self,reverse=true)==>sort list in ascending order.for descending order put reverse=false

expenses.sort()

print(expenses)

#def index(self,object)==>returns the index object(if the object is present)

index=expenses.index(14000)

print(index)

#copy()creates copy of the object

new_expenses=expenses#here the object which points to expenses is also pointed by new_expenses.so if value of is changed,the value of other is also changed

print(new_expenses)

new_expenses.pop()

print(expenses)

print(new_expenses)

#by using copy method it creates new object so if one is changed the other is not affected

new_expenses2=expenses.copy()

expenses.pop()

print(expenses)

print(new_expenses2)

#extend()

fruits=["apple","orange","mango"]

products=["onion","potato","brinjal"]

products.extend(fruits)

print(products)

#reverse()

fruits.reverse()

print(fruits)

products.reverse()

print(products)

#count()

