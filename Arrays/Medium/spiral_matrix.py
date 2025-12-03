from typing import List
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        op = []
        top,bottom = 0, len(matrix) - 1
        left,right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for i in range(left,right+1):
                op.append(matrix[top][i])
            top+=1
            if not top<=bottom or not left<=right:
                break      

            for i in range(top,bottom+1):
                op.append(matrix[i][right])
            right-=1
            if not top<=bottom or not left<=right:
                break  

            for i in range(right,left-1,-1):
                op.append(matrix[bottom][i])
            bottom-=1
            if not top<=bottom or not left<=right:
                break  

            for i in range(bottom,top-1,-1):
                op.append(matrix[i][left])
            left+=1
            if not top<=bottom or not left<=right:
                break  
        return op       
