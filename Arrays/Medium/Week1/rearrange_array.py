def rearrange_array(nums):
    op = [0] * len(nums)
    pos_ind = 0
    neg_ind = 1

    for i in range(len(nums)):
        if nums[i] < 0:
            op[neg_ind] = nums[i]
            neg_ind += 2
        else:
            op[pos_ind] = nums[i]
            pos_ind += 2
    return op  

nums = [3,1,-2,-5,2,-4]
print(rearrange_array(nums))
          