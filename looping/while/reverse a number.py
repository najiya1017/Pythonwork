num=int(input("Number:")) 

reverse=0

while(num!=0):

    digit=num%10

    reverse=reverse*10+digit

    num=num//10

print("Reversed Number=",reverse)