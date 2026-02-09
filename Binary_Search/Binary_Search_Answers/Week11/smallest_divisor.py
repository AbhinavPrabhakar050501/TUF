from typing import List
from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r = 1,max(nums)
        n = len(nums)
        op = r
        res = 0
        while l<=r:
            res = 0
            m = (l+r)//2
            print(m)
            for i in range(n):
                res += ceil(nums[i]/m)
            if res <= threshold:
                op = min(m,op)
                r = m - 1
            else:
                l = m + 1
        return op            
