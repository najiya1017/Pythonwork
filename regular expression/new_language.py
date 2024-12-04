from re import fullmatch

input_=input("Enter Variable name:")

#starting with an alphabet from p to t

#in second place must be a number \ by 3

#followed by anynumber alphabetsmnumbers,@

pattern="[p-tP-T][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,input_)

if matcher==None:

    print("Invalid")

else:

    print("valid")