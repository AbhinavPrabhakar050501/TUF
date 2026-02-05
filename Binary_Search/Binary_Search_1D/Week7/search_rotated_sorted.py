from typing import List
#Pattern 3- find left sorted or right sorted.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n - 1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            #find the right sorted part
            if nums[m] < nums[r]:
                if  nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1    
            else:#left sorted part
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l= m+1    
        return -1        
