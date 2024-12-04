#lambda function for finding cube of a number

cube=lambda num:num**3

print(cube(3))

#lambda function to add 2 numbers

add=lambda n1,n2:n1+n2

print(add(10,2))

#lambda function to substract 2 numbers

substract=lambda n1,n2:n1-n2

print(substract(10,2))

#to return string with maximum length

max_two=lambda str1,str2:str1 if str1>str2 else str2

print(max_two("Apple","Pinapple"))

#to return string with minimum length

min_two=lambda str1,str2:str1 if str1<str2 else str2

print(min_two("Apple","Pinapple"))

#smart sub

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(30,100))

