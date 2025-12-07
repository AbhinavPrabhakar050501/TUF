nums = [5,200,100,2,4,1,3,6]
# nums = [100,4,200,1,3,2]
# print(set(nums))
def long_seq(nums):
    numSet = set(nums)
    count,longest = 0,0
    for num in numSet:
        #start of sequence
        if (num-1) not in numSet:
            count = 1
            while (num+count) in numSet:
                count+=1
            longest = max(longest,count)
    return longest             

print(long_seq(nums))
