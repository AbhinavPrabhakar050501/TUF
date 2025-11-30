def count_good_numbers(n:int) -> int:
    MOD = 10**9 + 7
    def power(x,n):
        if n==0:
            return 1
        if n==1:
            return x
        if n<0:
            x = 1/x
            n = -n
        if n%2 == 0:
            return power(x*x,n//2) % MOD
        return x * power(x,n - 1) % MOD

    even_indices = (n+1)//2 
    odd_indices = n // 2
    return (power(5,even_indices)*power(4,odd_indices)) % MOD    

print(count_good_numbers(2))
