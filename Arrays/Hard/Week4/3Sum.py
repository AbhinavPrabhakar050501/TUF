from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #STEP 1:
        #build hashmap with pos :
        # pos = {}
        # for i in range(0,len(nums)):
        #     pos[nums[i]] = i
        # #{-1:0,0:1}                                                
        # print(pos)
        # l,r = 0,1
        # op = []
        # while r < len(nums):
        #     ans = 0 - nums[l] - nums[r]
        #     if ans in pos and pos[ans] != l and pos[ans] != r:
        #         op.append([nums[l],nums[r],ans])
        #     l=l+1
        #     r=r+1    

        # return op

        #better approach using hashset
        # ansset = set()
        # for i in range(0,len(nums)):
        #     hashset = set()
        #     for j in range(i+1,len(nums)):
        #         third = -(nums[i] + nums[j])

        #         if third in hashset:
        #             #we found a triplet
        #             triplet = tuple(sorted([nums[i],nums[j],third]))
        #             ansset.add(triplet)

        #         hashset.add(nums[j])    

        # return [list(triplet) for triplet in ansset]      

        #optimal approach using two pointers

        #Step 1 : sort the array
        #If same as prev number move forward
        # 
        # 2 pointers on from fornt and one from back
        # skip dups 
        #  

        n = len(nums)
        nums.sort()
        op = []

        for i in range(n):
            if i>0 and nums[i] == nums[i - 1]:
                continue

            l,r = i+1,n-1 
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    op.append([nums[i],nums[r],nums[l]])
                    
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1

                    l += 1 # and then skip dups
                    r -= 1    

                elif total < 0:
                    l+=1
                else:
                    r-=1

        return op        

obj = Solution()
three_summer = obj.threeSum(nums=[-1,0,1,2,-1,-4])

print(three_summer)





