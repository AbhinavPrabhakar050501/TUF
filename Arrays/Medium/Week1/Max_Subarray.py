#kadanes algorithm
# It states that sum will be zero
# if sum becomes less than zero
# meaning we do not need to consider negatives
# hence we get a negative we reset the position and continue

# PART - 1
def max_sub(nums):
    sum, max_sum = 0,nums[0]
    for i in range(len(nums)):
        sum += nums[i]
        max_sum = max(max_sum,sum)
        if sum<0:
            sum = 0
    return max_sum    

#PART -2 FOLLOW UP- What if multiple max sub arrays?? -> append it into a new list
#PART 2 Can you print the subarray that has the maximum sum?
def max_sub(nums):
    sum, max_sum = 0,nums[0]
    start = 0
    indexStart,indexEnd = 0,0
    for i in range(len(nums)):
        if sum<0:
            sum = 0
            start = i
        sum += nums[i]    
        # max_sum = max(max_sum,sum)
        if sum > max_sum:
            max_sum = sum
            indexStart = start
            indexEnd = i
    return max_sum,nums[indexStart:indexEnd+1]   

nums =  [2, 3, 5, -2, 7, -4]
# nums = [-2, -3, -7, -2, -10, -4]  
print(max_sub(nums))