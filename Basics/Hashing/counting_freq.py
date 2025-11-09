class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        hashmap = {}
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)

        op = []
        for key,value in hashmap.items():
            op.append([key,value])

        return op    