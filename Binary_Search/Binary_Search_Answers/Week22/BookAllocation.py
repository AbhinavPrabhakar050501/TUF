def findPages(arr, n, m):
    if m > n:
        return -1

    low = max(arr)
    high = sum(arr)

    while low <= high:
        mid = (low+high)//2

        students = countStudents(arr,mid)
        if students > m:
            low = mid+1
        else:
            high = mid-1
    return low           

def countStudents(arr,pages):
    pagesperstudent = 0; students = 1     

    for i in range(len(arr)):
        if arr[i] + pagesperstudent <= pages:
            pagesperstudent += arr[i]
        else:
            pagesperstudent = arr[i]   
            students += 1
    return students        