#Majority voting algo
from typing import List
def majorityElement(nums: List[int]) -> List[int]:
        # counter = {}
        # n = len(nums)
        # op = []
        # for num in nums:
        #     counter[num] = 1 + counter.get(num,0)

        # for key,value in counter.items():
        #     if value > n//3 : 
        #         op.append(key)

        # return op               
        
        #majority voting algo with 2 candidates
        candidate1,candidate2 = None, None #change from 0,0 to None, None as last edge case fails cause compare 0 and 0.
        count1,count2 = 0,0

        #first pass for finding the candidates
        for num in nums:
            #if candidate 1 loses count and the candidate is not the second one
            # we need to make a new candidate 1
            if count1 == 0 and num != candidate2:
                count1 = 1
                candidate1 = num

            elif count2 == 0 and num != candidate1:
                count2 = 1
                candidate2 = num

            elif candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

            else:
                count1 -= 1
                count2 -= 1

        op = []
        threshold = len(nums)//3

        #second pass for counting the occurences of the candidates
        count1 = count2 = 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1     

        if count1 > threshold:
            op.append(candidate1)
        if count2 > threshold:
            op.append(candidate2)

        return op     


print(majorityElement(nums =[3,2,3]))
