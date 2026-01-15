from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        indexStart,indexEnd = -1,-1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                indexStart,indexEnd = mid,mid
                store_mid = mid
                while mid-1 >= l and nums[mid-1] == target:
                    indexStart = mid - 1
                    mid = mid - 1
            
                mid = store_mid
                while mid+1 <= r and nums[mid+1] == target:
                    indexEnd = mid + 1
                    mid = mid + 1

                return[indexStart,indexEnd]

            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return [indexStart,indexEnd]   