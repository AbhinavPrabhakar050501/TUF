# def leaders(nums):
#     n = len(nums)
#     op = [nums[-1]] #last integer always will be present\
#     for i in range(n-2,-1,-1):
#         if nums[i] > nums[i+1:]: #another looop so O(n^2)
#             op.insert(0,nums[i])
#     return op        

# nums = [1, 2, 5, 3, 1, 2]
# # nums = [-3, 4, 5, 1, -4, -5]
# print(leaders(nums))

#optimized approach -> 2 pointers
def leaders(nums):
    n = len(nums)
    op = [nums[-1]] #last integer always will be present\
    r = nums[-1]
    for l in range(n-2,-1,-1):
        if nums[l] > r:
            r = nums[l] 
            # op.insert(0,nums[l])   not optimal become O(n^2)
            op.append(nums[l])

    return op.reverse()

# nums = [1, 2, 5, 3, 1, 2]
nums = [-3, 4, 5, 1, -4, -5]
print(leaders(nums))

