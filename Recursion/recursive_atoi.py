class Solution:
    def Atoi(self,s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        s = s.lstrip()

        i = 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i+=1
        elif s[i] == '+':
            sign = 1
            i+=1     

        num = 0

        def helper(s,i,sign,num):
            #reached the end of the loop or not a digit
            # BASE CASE    
            if i >= len(s) or not s[i].isdigit():
                return sign * num
            print(num)
            num = num*10 + int(s[i])

            if sign*num > INT_MAX:
                return INT_MAX
            elif sign*num <= INT_MIN:
                return INT_MIN 
            return helper(s,i+1,sign,num)
        
        return helper(s,i,sign,num)

# s = "4193 with words"        
s = "-12345"  
recursive_obj = Solution()
print(recursive_obj.Atoi(s))      