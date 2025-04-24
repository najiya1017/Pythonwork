def isAdditiveNumber(num):
    def is_valid(a, b, remaining):
        while remaining:
            total = str(a + b)
            if not remaining.startswith(total):
                return False
            remaining = remaining[len(total):]
            a, b = b, a + b
        return True
    num=str(num)
    n = len(num)
    for i in range(1, n // 2 + 1):
        for j in range(1, (n - i) // 2 + 1):
            a, b = num[:i], num[i:i + j]
            if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
                continue
            remaining = num[i + j:]
            if is_valid(int(a), int(b), remaining):
                return True
    return False

print(isAdditiveNumber(112358))
print(isAdditiveNumber(199100199))

