#records are stored in pairs of key:value 

#defined by {}

product={"id":1000,"title":"watch","price":2000,"brand":"casio"}

print(product["title"])

print(product["price"])

#update-key

product["price"]=3000

print(product["price"])

print(product)

product["brand"]="titan"

print(product["brand"])

product["use_by_date"]="12-2-2025"

product["offer"]=2500

print(product)

#check whether a key exist or not

if "price" in product:

    print("exist")

else:

    print("not exist")

#add 10 to offer ,if offer exist else add 20

if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)

#============================================================================================================================

#DICTIONARY METHODS

# get() to get value of key instead of  using square brackets.

employee={"eid":123,"name":"Reena","department":"Tester","age":24,"salary":25000}

print(employee.get("departmnt")) #doesn't show error,instead returns none and execute remaining code.

print("Test Message 1")

print("Test Message 2")

#pop(key)==>remove key value pair

employee.pop("age")

print(employee)

#keys()==>returns only key.

for k in employee.keys():

    print(k)

#values()==>fetch only values of key

for v in employee.values():

    print(v)

print(employee.keys())

print(employee.values())

#items()==>to get both keys and values.

for k,v in employee.items():

    print(k,v)

print(employee.items())

print(employee)

