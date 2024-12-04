number=input("Enter Number:")

digit_count=len(number)

number=int(number)

original=number

total=0

while(number!=0):

    digit=number%10

    sdigit=digit**digit_count

    total=total+sdigit

    number=number//10

# if total==original :

#     print("Armstrong Number")

# else:

#     print("Not Armstrong Number")

print("Armstrong number" if total==original else "Not Armstrong")