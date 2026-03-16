class Solution:
    def largestOddNumber(self, num: str) -> str:
        op = ""

        for i in range(len(num)-1,-1,-1):
            if int(num[i]) %2 == 0:
                continue
            elif int(num[i]) %2 != 0:
                op += num[0:i+1]
                break
        return op
        