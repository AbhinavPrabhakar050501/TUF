class Solution:
    def findRotations(self, nums):
        l,r = 0, len(nums) - 1
        while l<r:
            m = (l+r)//2
            #find the sorted array
            if nums[m] > nums[r]: #breakpoint exists on the right half
                l = m+1
            else:
                r = m-1
        return l #when low == high thats when we have found the smallest element        