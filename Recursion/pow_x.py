#This is tricky as normal linear recursion
#would fail hence O(n) would fail

#only solution is using O(log(n)) where we
#are fast exponentiation trick which says:

# half = helper(x,n//2)
# if n%2 == 0:
#     return half * half 
# else:
#     return half*half*x    

#formula: xn={(xn/2)2,(x(n//2))2×x,​if n is evenif n is odd​
def power(x,n):
    if n==0:
        return 1

    if n==1:
        return x

    if n<0:
        x = 1/x
        n = -n

    if n%2 == 0:
        return power(x*x,n//2)

    return x * power(x,n - 1)    


print(power(2,10))
print(power(-2,10))
print(power(2,-10))

