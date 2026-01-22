from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l,r = 0,len(nums)-1
        op = float('inf')
        while l <= r:#single elements so '='
            mid = (l+r)//2
            
            #break out early (not needed step)
            if nums[l] <= nums[r]:
                op = min(op,nums[l])
                break
            
            #find the sorted part
            if nums[l] <= nums[mid]:
                op = min(op,nums[l])
                l = mid+1
            else:
                op = min(op,nums[mid]) #dont get confused draw the prob..easy
                r = mid-1
        return op