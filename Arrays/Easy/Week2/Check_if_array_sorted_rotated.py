from typing import List
def sort_rot(nums:List[int]) -> bool:
    # if there are multiple drops it is false: algo
    n = len(nums)
    if n <= 2:
        return True

    drop = 0
    for i in range(n):
        if nums[i] > nums[(i+1)%n]: #Modulo lets us compare last → first and close the circle.
            drop += 1    
            if drop > 1:
                return False 
    return True 


print(sort_rot([3,4,5,1,2]))
print(sort_rot([2,3,1,4]))
