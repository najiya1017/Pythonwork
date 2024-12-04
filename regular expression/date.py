from re import fullmatch

date=input("Enter date:")

pattern="(0?[1-9]|[12][0-9]|3[01])"

matcher=fullmatch(pattern,date)

if matcher==None:

    print("Invalid")

else:
    print("Valid")