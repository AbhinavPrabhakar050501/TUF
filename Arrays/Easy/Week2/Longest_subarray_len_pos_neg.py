#for only positive and zeros;
#we can use sliding window approach

def longest_pos(nums,k):
    l = 0
    max_len = 0
    for r in range(len(nums)):
        if nums[l] + nums[r] == k:
            max_len = max(max_len,(nums[l:r+1]))
        elif nums[l] + nums[r] > k:
            l+=1     

    return max_len

print(longest_pos([10,5,2,7,1,9],15))
