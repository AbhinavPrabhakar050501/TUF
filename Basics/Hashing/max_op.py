class Solution:
    def mostFrequentElement(self, nums):
        hashmap = {}
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)

        #4:2,5:2,6

        max_op = 0
        most_freq = None
        for key,value in hashmap.items():
            if value > max_op:
                max_op = value
                most_freq = key
        return most_freq       