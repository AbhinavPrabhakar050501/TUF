#O(nlogn) approach
# def findMissingRepeatingNumbers(nums):
#         nums.sort()
#         A = B = 0
#         n = len(nums)

#         for i in range(n - 1):
#             if nums[i] == nums[i + 1]: # repeating
#                 A = nums[i]
#             elif nums[i + 1] > nums[i] + 1: # greater than 1
#                 B = nums[i] + 1

#         if B == 0:              # missing number is n, end of sequence
#             B = n

#         return [A, B]

#O(N) with maths approach(sum of n natural numbers)-> remember missing number we used the same
def findMissingRepeatingNumbers(nums):
    '''
    Expected sum = n(n+1)/2
    Expected square sum = n(n+1)(2n+1)/6
    '''
    n = len(nums)
    expected_sum = n*(n+1)//2
    expected_sum_sqr =  n * (n + 1) * (2*n + 1) // 6

    actual_sum = sum(nums)
    actual_sum_sqr = sum(x*x for x in nums)

    diff = actual_sum - expected_sum #A - B
    sq_diff = actual_sum_sqr - expected_sum_sqr # A² - B²

    sum_ab = sq_diff//diff #A+B(maths)

    A = (diff + sum_ab)//2
    B = A - diff

    return[A,B]    


print(findMissingRepeatingNumbers([3, 5, 4, 1, 1]))
print('*****')
print(findMissingRepeatingNumbers([1, 2, 3, 6, 7, 5, 7]))