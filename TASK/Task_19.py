import math

def maximumSumDivisible(nums):
    n = len(nums)
    f = [[-math.inf] * 3 for _ in range(n + 1)]
    f[0][0] = 0
    for i, x in enumerate(nums, 1):
        for j in range(3):
            f[i][j] = max(f[i - 1][j], f[i - 1][(j - x % 3) % 3] + x)
    return f[n][0]

arr = list(map(int, input("nums: ").split(",")))
print(maximumSumDivisible(arr))
