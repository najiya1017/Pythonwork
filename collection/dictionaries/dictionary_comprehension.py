arr=[10,20,30,40,2,3,10,30,2]

squares={}

for i in arr:

    squares[i]=i**2

print(squares)

#using dictionary comprehension

result={num:num**2 for num in arr}

print(result)

#cubes

cubes={num:num**3 for num in arr}

print(cubes)

#even squares and odd cubes

even_squares={num:num**2 for num in arr if num%2==0}

print(even_squares)

odd_cubes={num:num**3 for num in arr if num%2!=0}

print(odd_cubes)

#frequency counts of items

frequency_count={num:arr.count(num) for num in arr}

print(frequency_count)

