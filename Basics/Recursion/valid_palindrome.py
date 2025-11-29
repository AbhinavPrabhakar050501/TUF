def helper(l,r):
    if l >= r:
        return True #base case
    
    while l>r and s[l].isalnum() != True: #edge cases
        l += 1
    while l>r and s[r].isalnum() != True:
        r -= 1

    if s[l].lower() == s[r].lower():
        return helper(l+1, r-1)
    else:
        return False

s = "abccba"
# s = "df"
print(helper(l=0 , r = len(s)-1))      