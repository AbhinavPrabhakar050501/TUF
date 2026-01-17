from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m

            if nums[m] < target:
                l = l + 1
            else:
                r = r - 1        

        if nums[m] != target:
            if nums[m] < l:
                return l
            else:
                return r + 1


object = Solution()
print(object.searchInsert(nums=[0,0,1,2,3,4,4,4,5,5],target=4))                 