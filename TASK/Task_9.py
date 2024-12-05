# Given an array of intervals where intervals [i] = [starti, endil, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Example 1:
# Input: intervals = [[1,31, [2,61, [8, 10], [15, 18]]
# Output: [[1,61, [8,101, [15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6] •
# Example 2:
# Input: intervals = [[1,41, [4,51]
# Output: [[1,511
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.





def not_overlapping(intervals):
    skip=False
    new_list=[]
    for i in range(len(intervals)):
        if skip==True:
            skip=False
            continue
        elif i!=len(intervals)-1:
            current_item=intervals[i]
            next_item=intervals[i+1]
            if current_item[1]>=next_item[0]:
                new_list.append([current_item[0],next_item[1]])
                skip=True
            else:
                new_list.append(current_item)
        else:
            new_list.append(intervals[i])
    return new_list     

print(not_overlapping([[1,3], [2,6], [8, 10], [15, 18]]))   
print(not_overlapping([[1,4], [4,5]]))