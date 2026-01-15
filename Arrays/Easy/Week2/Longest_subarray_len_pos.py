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

#for negatives as well.
def get_longest_subarray( a, k):
        n = len(a)
        pre_sum_map = {}  # Dictionary to store prefix_sum -> first index
        sum_so_far = 0    # Running sum
        max_len = 0       # Max length of subarray with sum = k

        for i in range(n):
            sum_so_far += a[i]  # Update running sum

            # Case 1: Entire subarray from index 0 to i has sum = k
            if sum_so_far == k:
                max_len = i + 1

            # Case 2: If (sum_so_far - k) exists in map, we found a valid subarray
            rem = sum_so_far - k
            if rem in pre_sum_map:
                length = i - pre_sum_map[rem]
                max_len = max(max_len, length)

            # Store the first occurrence of the current prefix sum
            if sum_so_far not in pre_sum_map:
                pre_sum_map[sum_so_far] = i

        return max_len