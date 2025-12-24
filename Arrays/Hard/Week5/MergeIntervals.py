from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #step1 sort the array to prevent issues
        intervals.sort()
        # print(intervals)
        #have the output store the first interval
        merged = [intervals[0]]
        for interval in intervals:
            #case 1 if the existing 2nd element is less than the new intervals first element....
            #append 
            if merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                #else we have found that this sits in the interval so replace the element,
                #with the intervals bigger element.
                merged[-1][1] = max(merged[-1][1] , interval[1])    
        return merged    