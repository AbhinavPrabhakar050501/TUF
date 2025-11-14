def count_good_numbers(n:int) -> int:
    MOD = 10**9 + 7
    def pow(x,y):
        if y == 0: #x^0 = 1
            return 1
        half = pow(x,y//2)
        if y % 2 == 0:
            return (half * half) % MOD
        else:
            return (half * half * x) % MOD

    even_indices = (n+1)//2 
    odd_indices = n // 2

    return count_good_numbers(pow(5,even_indices)*pow(4,odd_indices)) % MOD    

