def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    index = -1
    #step 1: find the break point
    for i in range(len(nums)-2,-1,-1):
        if nums[i]<nums[i+1]:
            index = i
            break
            
    #edge case if the sequence is the last one
    if index == -1:
        nums.reverse()
        return

    #swap the first element with the index 
    for i in range(len(nums)-1,index,-1):
        if nums[i]>nums[index]:
            nums[i],nums[index] = nums[index],nums[i]
            break
    #reverse the remaining
    nums[index+1:] = reversed(nums[index+1:])
nums = [1,2,3]
nums = [3,2,1,4]
nextPermutation(nums)
print(nums)