# nums = [0,1,2,3,4,5]
# print(nums[2:4])
# #wont work for negatives
# l,r = 0,1
# k = 6
# op = 0

# #can improve by removing repetitve sum calls
# while r < len(nums) - 1:
#     if sum(nums[l:r+1]) == k:
#         op+=1
#         l+=1
#         r+=1 
#     elif sum(nums[l:r+1]) < k:
#         r+=1
#     else:
#         l+=1

# print(op)
from typing import List
def subarraySum(nums: List[int], k: int) -> int:
    prevSum = 0
    count = 0
    prevMap = {}
    prevMap[0] = 1 #default base case zero has occured once

    for num in nums:
        prevSum += num #adding previous sums
        result = prevSum - k #finding the result of total - prev to see if present already

        if result in prevMap:
            count += prevMap[result] #increasing the count from map,not updating map directly

        prevMap[prevSum] = prevMap.get(prevSum,0) + 1 #add every prefixsum to check again.

    return count

nums = [1,2,3] 
k = 3
print(subarraySum(nums,k))
