#GPT soln
class Solution:
    def countInversions(self, arr):
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums, 0

            mid = len(nums) // 2
            left, inv_left = merge_sort(nums[:mid])
            right, inv_right = merge_sort(nums[mid:])

            merged, cross_inv = merge(left, right)
            return merged, inv_left + inv_right + cross_inv

        def merge(left, right):
            i = j = 0
            merged = []
            inv_count = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    inv_count += len(left) - i
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, inv_count

        _, total_inversions = merge_sort(arr)
        return total_inversions

#STrivers soln: better understood.
def merge(arr, low, mid, high):
    # Temporary array
    temp = []

    # Starting indices of left and right halves
    left = low
    right = mid + 1

    # Variable to count inversions
    cnt = 0

    # Merge elements in sorted order
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)  # Count inversions
            right += 1

    # Copy remaining elements of left half
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Copy remaining elements of right half
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy back to original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return cnt

def mergeSort(arr, low, high):
    # Variable to count inversions
    cnt = 0

    if low >= high:
        return cnt

    mid = (low + high) // 2

    # Count inversions in left half
    cnt += mergeSort(arr, low, mid)
    # Count inversions in right half
    cnt += mergeSort(arr, mid + 1, high)
    # Count inversions during merge
    cnt += merge(arr, low, mid, high)

    return cnt

def numberOfInversions(arr):
    return mergeSort(arr, 0, len(arr) - 1)

# Input array
a = [5, 4, 3, 2, 1]

# Count inversions
cnt = numberOfInversions(a)
print("The number of inversions are:", cnt)
