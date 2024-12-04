begin=int(input("Begin:"))

end=int(input("End:"))

if end<begin:

  begin,end=end,begin

i=begin

while(i<=end):

  if(i%2!=0):

    print(i)

  i+=1
