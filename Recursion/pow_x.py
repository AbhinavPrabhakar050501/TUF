#This is tricky as normal linear recursion
#would fail hence O(n) would fail

#only solution is using O(log(n)) where we
#are fast exponentiation trick which says:

# half = helper(x,n//2)
# if n%2 == 0:
#     return half * half 
# else:
#     return half*half*x    


def Pow(x,n):
    if n == 0:
        return 1
    if n < 0 :
        x = 1/x
        n = -n #make postive

    half = Pow(x,n//2)
    if n % 2:
        return half*half
    else:
        return half*half*x
    
    return Pow(x,n)
