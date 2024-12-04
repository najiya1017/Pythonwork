from re import fullmatch

pan_number=input("Enter pan card number:")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pan_number)

if matcher==None:

    print("Invalid")

else:

    print("valid")