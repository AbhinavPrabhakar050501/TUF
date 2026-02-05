from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #index based prob and remember
        #you have to eliminate one half 
        #thats how you should think
        n = len(nums) - 1
        if n == 0:
            return nums[0]
        #first element check
        if nums[0] != nums[1]:
            return nums[0]

        #last element check
        if nums[n] != nums[n-1]:
            return nums[n]

        l,r = 1,n-1 

        while l<=r:
            m = (l+r)//2      
            if nums[m-1] != nums[m] != nums[m+1]:
                return nums[m] #this is the single element

            #detect which half we are at using the indexes
            # if we are the left half we eliminate the left half
            # how to know if we are in the left half, the left of
            # odd index will be even and vice versa

            if ((m%2 == 1 and (nums[m-1] == nums[m])) or (m%2 == 0 and (nums[m] == nums[m+1]))):
                #eliminate the left half
                l = m + 1
            else:
                r = m - 1
        
        return -1              


        