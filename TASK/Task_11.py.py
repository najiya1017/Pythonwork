# Write a program to determine if a given number is a happy number. A number is called a happy number if repeatedly
# replacing the number by the sum of the squares of its digits eventually leads to 1. If it enters a cycle that does not include 1, it is not a happy number.
# Example Input and Output:
# Input: 19
# Output: 19 is a happy number.
# Explanation:
# 12 + 92 = 82
# 82
# + 22 = 68
# 62
# + 82 = 100
# 12 + 02 + 02 = 1
# Input: 4
# Output: 4 is not a happy number.
# Explanation:
# 42 = 16
# 12
# + 62 = 37
# 32
# + 72 = 58
# 52 + 82 = 89
# (and it enters a cycle without reaching 1)
def sum_of_squares(num):
    result=0
    while num!=0:
        digit=num%10
        result=result+digit**2
        num=num//10
    return result

def is_happy_number(num):
    result=sum_of_squares(num)
    ending_numbers=(0,4,16,20,37,42,58,89,145)
    while (True):
        if result==1:
            return True
            break
        elif result in ending_numbers:
            return False
            break
        else:
            result=sum_of_squares(result)
            
num=int(input("Enter Number:"))
result=is_happy_number(num)
print("Happy number" if result==True else "Not happy number" )


