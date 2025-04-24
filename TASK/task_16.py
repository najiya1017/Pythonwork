n=int(input("n:"))
numbers=[str(i) for i in range(1,n+1)]
lexicographical=sorted(numbers,key=lambda num:int(num[0]))
print(lexicographical)