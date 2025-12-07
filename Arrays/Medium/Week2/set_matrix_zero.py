# nums = [[1,1,1],[1,0,1],[1,1,1]]
#THIS IS MARKING THE ENTIRE COL AND ROW METHOD
# CAUSE O(M*N*(M+N)) where M+N is the repeated scans, we can 
# improve on this.
# same but written in A2Z- Time Complexity: O(m * n * (m + n)), We iterate through every cell (m * n), 
# and for each zero,
# we potentially mark its entire row (O(n)) and column (O(m)), leading to O(m * n * (m + n)) overall.
# rows = len(nums)
# cols = len(nums[0])
# for i in range(rows):
#     for j in range(cols):
#         if nums[i][j] == 0:
#             #need to mark the entire col
#             for c in range(cols):
#                 if nums[i][c] != 0: #if the number present is not already zero
#                     nums[i][c] = -1

#             for r in range(rows):
#                 if nums[r][j]  != 0:
#                     nums[r][j] = -1        

# for i in range(rows):
#     for j in range(cols):
#         if nums[i][j] == -1:
#             nums[i][j] = 0

#we improve the above solution by using space making space
# complexity O(m*n) and reducing time to O(m*n)   
# now to make the problem constant space
# by reusing the input matrix itself as the marker
# row = [0] * rows
# col = [0] * cols

# for i in range(rows):
#     for j in range(cols):
#         if nums[i][j] == 0:
#             row[i] = 1
#             col[j] = 1

# for i in range(rows):
#     for j in range(cols):
#         if row[i] == 1 or col[j] == 1:
#             nums[i][j] = 0

# now to make the problem constant space
# by reusing the input matrix itself as the marker
# we can use the firstrow and firstcol as markers
# so basically we first go through the firstrow and firstcol 
# and have a separate marker for these to check if we need to 
# mark or no
# after that we go inside from the 1,m and 1,n row col respectively
# and then decide mark the firstrow and first col based on the matrix
# and we keep doin this till the end of matrix
#T(n) = O(m*n)
#space = O(1)
from typing import List
def matrix_zero(matrix:List[List[int]]) -> None: 
    #  to check if first row and col need to be zeroed
    first_row_zero = False
    first_col_zero = False

    rows = len(matrix)
    cols = len(matrix[0])

    # first loop to check firstrow and col to zerod 
    # or no cause we need to set it as a marker
    for i in range(cols):
        if matrix[0][i] == 0:
            first_row_zero = True

    # now the same for firstcol
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True


    #now going through the matrix and settign the first row or col to 0,
    # as they are markers now
    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    #now whatever marked using the firstrow/col set that row/col to 0
    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    #now for the first row and col
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0 

matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix_zero(matrix)
print(matrix)
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix_zero(matrix)
print(matrix)


