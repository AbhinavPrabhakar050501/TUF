class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        op = ""
        level = 0
        for i in s:
            if i == "(":
                if level > 0: #if we are in the inside level
                    op+=i
                level += 1
            else:
                level -= 1
                if level > 0: # if we are still inside
                    op+=i       
        return op