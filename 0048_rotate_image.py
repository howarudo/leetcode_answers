# Problem link: https://leetcode.com/problems/rotate-image/
# Date: 20223/09/12
# Big-O: O(n^2)
# Overview:
#   - Rotation of the whole matrix is seen as rotation of individual layers
#   - Rotation of individual layers are then seen as rotations of group of rotations of 4 grids
#   - So, having a while loop (rotation of layers) and a for loop (rotation of groups of 4) will solve it!
# <============ SOLUTION ============>

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            top, bot = l, r
            for i in range(r - l):
                temp = matrix[top][l + i]

                matrix[top][l + i] = matrix[bot - i][l]
                matrix[bot - i][l] = matrix[bot][r - i]
                matrix[bot][r - i] = matrix[top + i][r]
                matrix[top + i][r] = temp
            l += 1
            r -= 1
