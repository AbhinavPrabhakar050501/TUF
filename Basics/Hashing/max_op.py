class Solution:
    def mostFrequentElement(self,nums):
        hashmap = {}
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)

        #4:2,5:2,6

        max_op,min_op = 0,len(nums)
        most_freq,least_freq = None,None
        for key,value in hashmap.items():
            if value > max_op:
                max_op = value
                most_freq = key
            if value < min_op:
                min_op = value
                least_freq = key        


        return most_freq,least_freq     

nums = [1,1,2,2,3,1,3,2,0]
count_obj = Solution()
print(count_obj.mostFrequentElement(nums))            