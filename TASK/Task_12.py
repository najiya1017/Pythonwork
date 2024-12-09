def is_prime(num):
    is_prime=True
    for i in range(2,(num//2)+1):
        if num%i==0:
            is_prime=False
    return is_prime

def is_ugly(num):
    is_ugly=False
    if num==1:
        is_ugly=True

    if num%2==0 or num%3==0 or num%5==0:
        is_ugly=True

    for i in range(7,(num//2)+1):
        if is_prime(i) and num%i==0:
            is_ugly=False

    return is_ugly


num=int(input("n:"))
print(is_ugly(num))



#or

def is_ugly(num):
    # 0 and negative numbers are not considered ugly
    if num <= 0:
        return False
    
    # Divide the number by 2, 3, and 5 as long as it's divisible
    for factor in [2, 3, 5]:
        while num % factor == 0:
            num //= factor
    
    # If the remaining number is 1, it's an ugly number
    return num == 1

# Example usage
number = int(input("Enter a number to check if it's an ugly number: "))
if is_ugly(number):
    print(f"{number} is an ugly number.")
else:
    print(f"{number} is not an ugly number.")