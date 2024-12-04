arr=[2,4,5,6,7,3]

cubes=[]

for num in arr:

    cubes.append(num**3)    

print(cubes)

#list comprehension syntax=[return loop condition]

cubes=[num**3 for num in arr]

print(cubes)

squares=[num**2 for num in arr]

print(squares)

#if there is condition==>filter,no.of inputs!=no.of outputs

#if there is no condition==>maping,no.of inputs==no.of outputs

#reduce-max,min,sum,product

odd_numbers=[num for num in arr if num%2!=0]

print(odd_numbers)

gt_than_five=[num for num in arr if num>5]

print(gt_than_five)

#return num+1 if num>5 else num-1

map_num=[num+1 if num>5 else num-1 for num in arr]

print(map_num)

text=["apple","orange","iphone","potato"]

vowels=['a','e','i','o','u']

vowls=[w for w in text if w[0] in vowels]

print(vowls)   

consonants=[w for w in text if w[0] not in vowels]

print(consonants)   

#longest word

long=max([len(w) for w in text])

print(long)

longest_word=[w for w in text if len(w)==long]

print(longest_word)



