#kadanes algorithm
# It states that sum will be zero
# if sum becomes less than zero
# meaning we do not need to consider negatives
# hence we get a negative we reset the position and continue

# PART - 1
def max_sub(nums):
    for i in range(len(nums)):
        sum, max_sum = 0,0
        if sum<0:
            sum = 0
        sum = nums[i]    
        max_sum = max(max_sum,sum)
    return max_sum    

#PART -2 FOLLOW UP- What if multiple max sub arrays??
