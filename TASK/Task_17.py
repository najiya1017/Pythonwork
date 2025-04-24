# Given an integer n, return the smallest prime palindrome greater than or equal to n.
# An integer is prime if it has exactly two divisors: 1 and itself. Note that 1 is not a prime number.
# • For example, 2, 3, 5, 7, 11, and 13 are all primes.
# An integer is a palindrome if it reads the same from left to right as it does from right to left.
# • For example, 101 and 12321 are palindromes.
# The test cases are generated so that the answer always exists and is in the range [2, 2 * 108] -
# Example 1:
# Input: n = 6
# Output: 7
# Example 2:
# Input: n = 8
# Output: 11
# Example 3:
# Input: n = 13
# Output: 101




def primePalindrome(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    while True:
        if is_prime(n) and is_palindrome(n):
            return n
        n += 1


n=int(input("n:"))
print(primePalindrome(n))