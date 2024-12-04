from re import fullmatch

aadhar=input("Enter adhar number:")

pattern="[2-9]{1}[0-9]{3} [0-9]{4} [0-9]{4}"

matcher=fullmatch(pattern,aadhar)

if matcher==None:

    print("Invalid")

else:

    print("Valid")