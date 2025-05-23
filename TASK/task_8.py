
def multiplication(nums):
    n=len(nums)
    answers=[1]*n
    prefix=1
    for i in range(n):
        answers[i]=prefix
        prefix*=nums[i]

    suffix=1

    for i in range(n-1,-1,-1):
        answers[i]*=suffix
        suffix*=nums[i]

    return answers

print(multiplication([1,2,3,4]))
print(multiplication([-1,1,0,-3,3]))