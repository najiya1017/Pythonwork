from re import fullmatch

user_input=input("Enter mobile number:")

pattern="(91)?[0-9]{10}"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("Invalid")

else:

    print("Valid")