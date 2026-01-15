from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        #Merge sort, count inversions and merge algo
        # i use 3 diff pointers to solve the same.

        def mergeSort(nums,low,high):
            count = 0
            if low>=high:
                return count
            mid = (low+high)//2
            count += mergeSort(nums,low,mid)
            count += mergeSort(nums,mid+1,high)
            count += countInversions(nums,low,mid,high)
            merge(nums,low,mid,high)

            return count 

        def countInversions(nums,low,mid,high):
            right = mid + 1
            count = 0
            for i in range(low,mid+1):
                while(right <= high and nums[i] > 2*nums[right]):
                    right = right + 1
                count = count + (right - (mid + 1))
            return count        

        def merge(nums,low,mid,high):
            left = low
            right = mid + 1
            temp = []
            
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right+=1

            while left <= mid:
                temp.append(nums[left])
                left += 1

            while right <= high:
                temp.append(nums[right])
                right +=1

            for i in range(low,high+1):
                nums[i] = temp[i - low]           

        return mergeSort(nums,0,len(nums) - 1)    

nums = [1,3,2,3,1]
obj = Solution()
print(obj.reversePairs(nums))