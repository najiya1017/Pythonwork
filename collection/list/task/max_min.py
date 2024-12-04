arr=[1,5,7,8,9,10]

max=0

min=arr[0]

for i in arr:

    if i>max:

        max=i

    if i<min:

        min=i

print(f""" 
max:{max}
min:{min}
""")