'''
Docstring for Binary_Search.Binary_Search_Answers.Week11.aggressive_cows

NEW PATTERN with BS where we need to find the min of max or max of min,

'''

def aggressiveCows(stalls, k):
    stalls.sort()
    def canplacecow(stalls,no_of_cows_available,distance):
        no_of_cows = 1
        last_stall = stalls[0]
        for i in range(len(stalls)):
            if stalls[i] - last_stall >= distance:
                no_of_cows += 1
                last_stall = stalls[i]
            if no_of_cows >= no_of_cows_available:
                return True
        return False            

    #this range im not very convinced
    maximum = stalls[-1] - stalls[0]   
    ans = 0 
    #BF
    # for i in range(1,maximum+1):
    #     if canplacecow(stalls,k,i) == True:
    #         ans = i
            

    # return ans

    #BS
    l = 0
    r = maximum
    while l<=r :
        m = (l+r)//2
        if canplacecow(stalls,k,m) == True:
            ans = m
            l = m + 1
        else:
            r = m - 1
    return ans            
