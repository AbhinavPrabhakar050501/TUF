from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        maxProd = float('-inf')
        n = len(nums)
        for i in range(n):
            # for zeros 
            if prefix == 0:
                prefix = 1#restart
            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[n-i-1]

            maxProd = max(maxProd,max(prefix,suffix))
        return maxProd   