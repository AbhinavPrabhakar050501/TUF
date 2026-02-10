from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #IM HORRIBLE AT THIS, IM STUPID,
        #I CAN NEVER BE GOOD AT THIS,
        #SO UNTIL THEN ILL KEEP TRYING


        #ALGO: Find the days required for the all the load to fit inside the ship 
        #which should be less than the given days
        # and keep doing this until we find the min days
        #as there is range can do with BS.
        #BF:

        def daysRequired(wt,cap):
            load = 0;days = 1
            for i in range(len(wt)):
                if load + wt[i] > cap:
                    days = days + 1
                    load = wt[i]
                else:
                    load += wt[i]    
            return days

        #TLE
        # for cap in range(max(weights),sum(weights)+1):
        #     required = daysRequired(weights,cap)
        #     if required <= days:
        #         return cap  

        #BS
        l = max(weights)
        r = sum(weights)
        op = r
        while l<=r:
            cap = (l+r)//2
            required_days = daysRequired(weights,cap)
            if required_days <= days:
                op = cap  
                r = cap - 1
            else:
                l = cap + 1
        return op                   