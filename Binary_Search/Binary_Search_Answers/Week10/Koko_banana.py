class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # ini_k = 1

        # while ini_k <= max(piles):
        #     hours_taken = 0
        #     for b in piles:
        #         hours_taken += ceil(b/ini_k)

        #     if hours_taken <= h:
        #         return ini_k
        #     ini_k+=1

             
        l,r = 1,max(piles)
        op = r
        while l <= r:
            hours_taken = 0   
            m = (l+r)//2    
            
            for b in piles:
                hours_taken += ceil(b/m)

            if hours_taken <= h:
                op = m
                r = m - 1
            else:
                l = m + 1
        return op           


        