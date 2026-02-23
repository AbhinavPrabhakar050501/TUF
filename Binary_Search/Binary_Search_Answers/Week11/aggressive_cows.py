'''
Docstring for Binary_Search.Binary_Search_Answers.Week11.aggressive_cows

NEW PATTERN with BS where we need to find the min of max or max of min,

'''

def aggressiveCows(stalls, k):
    
    def canplacecow(stalls,cows_available,distance):
        no_of_cows_placed = 1 # KEEP COUNT OF HOW MANY COWS ARE PLACED
        last = stalls[0]
        for i in range(len(stalls)):
            if stalls[i] - last >= distance:
                no_of_cows_placed += 1
                last = stalls[i]
            #if we placed all the cows already
            if no_of_cows_placed >= cows_available:
                return True
        
        return False

            

    stalls.sort()
    l = 1
    r = stalls[-1] - stalls[0] #THE MAX RANGE CAN ONLY BE BETWEEN THE LAST AND FIRST 
    ans = 0
    while l <= r:
        mid = (l+r)//2    

        if canplacecow(stalls,k,mid) == True:
            ans = mid
            l = mid + 1
            
        else:
            r = mid - 1
            
        
    return ans    
