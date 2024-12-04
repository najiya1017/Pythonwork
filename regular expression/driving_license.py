from re import fullmatch

dr_license=input("Enter license number:")

pattern="(KL)[0-9]{2}\s[0-9]{4}[0-9]{7}"

matcher=fullmatch(pattern,dr_license)

if matcher==None:

    print("Invalid")

else:

    print("Valid")