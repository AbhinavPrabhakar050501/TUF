from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #dont need rows and cols as it is a square
        # rows,cols = len(matrix),len(matrix[0])
        n = len(matrix)
        #step 1 : transpose
        for i in range(n):
            #i+1,n to avoid double swaps and not touch diagonals.
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #step 2 : reverse each row        
        for i in range(n):
            matrix[i].reverse()

        