begin=int(input("Begin:"))

end=int(input("End:"))

reverse=False

if begin>end:

    reverse=True

i=begin

while(i!=end):

    if(i%2==0):

        print(i)

    if (reverse==True):

        i=i-1

    else:

        i=i+1

