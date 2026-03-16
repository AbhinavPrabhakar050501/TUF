
class Solution:
    def reverseWords(self, s: str) -> str:
        #BF
        s = s.strip()
        op = ""

        l = 0
        op = []
        for r in range(len(s)):
            if s[r] == s[r-1] == ' ':
                continue
            elif s[r] == ' ':
                op.append(s[l:r])
                l = r+1

        op.append(s[l:r+1])
        print(op)
        op2 = ""
        for word in reversed(op):
            word = word.strip()
            op2+= word+' '

        op2 = op2.strip()

        return op2      

        #BS 
        
          
        