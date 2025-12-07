#Create a one pass algo
# we can do with three variables as well keeping count of 
# 0s,1s and 2s but need to open three separate loops and use
# array indexing 


#one pass algo is using three pointer approach.
#sort colors arranged in R,G,B => 0,1,2
def sort_colors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    l,m,r = 0,0,len(nums) - 1
    while m <= r:
        if nums[m] == 0:
            nums[m],nums[l] = nums[l],nums[m]
            m+=1
            l+=1
        elif nums[m] == 1:
            m+=1
        else:
            nums[m],nums[r] = nums[r],nums[m]
            r -= 1


nums = [1, 0, 2, 1, 0]
print(sort_colors(nums))
print(nums)