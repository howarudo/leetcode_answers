# Problem link: https://leetcode.com/problems/number-of-islands/
# Date: 2023/10/01
# Big-O: O(n*m)
# Overview:
#   - Fill islands first then continue the for loop
#   - When meet new island, then increment counter
#   -
# <============ SOLUTION ============>

# 2023/10/01 OK with hints
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def fill(i, j):
            if i < 0 or j <0 or i >= row_num or j >= col_num or (i, j) in visited or grid[i][j] == "0":
                return None
            visited.add((i, j))
            fill(i-1, j)
            fill(i+1, j)
            fill(i, j-1)
            fill(i, j+1)
            return None

        row_num, col_num = len(grid), len(grid[0])
        counter = 0
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == "1":
                    if (i, j) not in visited:
                        counter += 1
                    fill(i, j)
        return counter
