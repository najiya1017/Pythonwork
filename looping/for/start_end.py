start=int(input("Start:"))

end=int(input("End:"))

step=1 if start<end else -1

END=end+1 if start<end else end-1

for num in range(start,END,step):

    print(num)