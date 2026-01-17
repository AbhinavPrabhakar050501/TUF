from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,len(nums) - 1

        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1             
        return -1 
    

object = Solution()
print(object.search([0,0,1,2,3,4,4,4,5,5],4))        