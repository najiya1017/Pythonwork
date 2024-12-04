from re import fullmatch

user_input=input("Enter variable name:")

pattern="[a-zA-Z][a-zA-z0-9_]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("Invalid")

else:

    print("Valid")