from re import fullmatch

gmail=input("enter mail id:")

pattern="[a-z][a-z0-9]{5,63}@gmail.com"  

matcher=fullmatch(pattern,gmail)

if matcher==None:

    print("Invalid")

else:

    print("Valid")