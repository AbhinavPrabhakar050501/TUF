def max_length_sub_array_sum_0(nums,k=0):
    s = 0
    hashmap = {}
    maxsum = 0

    for i in range(len(nums)):
        s += nums[i]

        if s == 0:
            maxsum = i + 1#simple traverse so best length
        else:
            if s in hashmap:
                maxsum = max(maxsum, i - hashmap[s])
            else:
                hashmap[s] = i

    return maxsum            

print(max_length_sub_array_sum_0([9, -3, 3, -1, 6, -5]))