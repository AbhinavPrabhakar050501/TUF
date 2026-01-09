def merge(arr, low, mid, high):
    # Temporary array
    temp = []

    # Starting indices of left and right halves
    left = low
    right = mid + 1


    # Merge elements in sorted order
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
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


def mergeSort(arr, low, high):
    if low >= high:
        return 

    mid = (low + high) // 2

    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)

arr = [5, 2, 8, 4, 1]    

mergeSort(arr ,low = 0,high =len(arr)-1)
print(arr)