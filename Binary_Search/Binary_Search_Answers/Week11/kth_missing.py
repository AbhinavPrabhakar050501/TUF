from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        # BF some logic this one, keep adding to k for those missing spots and when its above return the answer.
        # for num in arr:
        #     if num <= k:
        #         k += 1  # Increase k since num is not missing
        #     else:
        #         break  # Stop if num is greater than k
        # return k

        #BS some crazy brain you need to come up with this.
        l,r = 0, len(arr) - 1

        while l<=r:
            mid = (l+r)//2
            missing = arr[mid] - (mid + 1) #the value at the index vs what value should be there at the index + 1

            if missing < k:
                l = mid + 1  
            else:
                r = mid - 1   

        return k+1+r #l+k

