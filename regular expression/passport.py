from re import fullmatch

passport=input("Enter passport number:")

pattern=r"[A-Z][1-9][0-9]\d{4}[1-9]\s?"

matcher=fullmatch(pattern,passport)

if matcher==None:

    print("Invalid")

else:

    print("Valid")