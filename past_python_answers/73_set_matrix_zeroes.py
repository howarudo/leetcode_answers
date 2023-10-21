# Problem link: https://leetcode.com/problems/set-matrix-zeroes/
# Date: 20223/09/15, 2023/10/1
# Big-O: Computation: O(m*n), Spacial: O(1)
# Overview:
#   - Use first row and first column as a placeholder for 0s if detected
#   - Check every element, and change placeholder if 0 is encountered
#   - After checking, change whole rows or columns if the palceholder is 0
# <============ SOLUTION ============>

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # placeholder will hold bool if first row has 0
        placeholder = False
        row_num, col_num = len(matrix), len(matrix[0])
        for i in range(row_num):
            for j in range(col_num):
                if matrix[i][j] == 0:
                    if i != 0:
                        matrix[i][0] = 0
                    else:
                        placeholder = True
                    matrix[0][j] = 0

        for i in range(1, row_num):
            if matrix[i][0] == 0:
                matrix[i] = [0] * col_num

        for j in range(1, col_num):
            if matrix[0][j] == 0:
                for i in range(1, row_num):
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(row_num):
                matrix[i][0] = 0

        if placeholder:
            matrix[0] = [0] * col_num
