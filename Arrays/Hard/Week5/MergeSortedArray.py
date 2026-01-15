from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[i+1] = nums2[i]
        # for i in range(n):
        #     if nums1[i] <= nums2[i]:
        #         nums1[i] = nums1[i]
        #     else:    
        #         nums1[i],nums2[i] = nums2[i],nums1[i] 

        # nums1[m+n] = nums2[i]
        # i,j = 0,0
        # while j:
        #     if nums1[i] > nums2[j]:
        #         nums1[i],nums2[j] = nums2[j],nums1[i]
        #         i+=1
        #     elif nums1[i] < nums2[j]:
        #         i+=1   
        #     else:
        #         j+=1     

        #similar to dutch problem
        i = m - 1
        j = n - 1
        k = m+n - 1

        #The loop condition should be tied to the array being copied
        #NOT to pointer relationships like i < k
        
        #Loop while nums2 still has elements
        # and j and i cant be negative
        while j>=0:
            if i>=0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]    
                j-=1
            k-=1
            

nums1 = [1,2,2,3,3,0,0,0,0]
nums2 = [2,2,3,4]
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
obj = Solution()
obj.merge(nums1,5,nums2,4)         
print(nums1)