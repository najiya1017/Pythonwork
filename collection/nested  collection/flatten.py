arr=[
    [10,20],
    [20,30],
    [30,40],
    [40,50]
]

flatten=[num for lst in arr for num in lst]

print(flatten)

#number greater than 25

num_gt_25=[num for lst in arr for num in lst if num>25]

print(num_gt_25)