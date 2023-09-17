# Problem link: https://leetcode.com/problems/word-search/description
# Date: 2023/09/17
# Big-O: O(m * n * 4^(s)), m and n are dimensions of board, s is the lenght of word
# Overview:
#   - depth first search. loop through all the elements in the board
#   - Base cases are, when element indices are out of bounds, not equal to word, or visited path
# <============ SOLUTION ============>

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        col_num, row_num = len(board), len(board[0])
        path = set()
        def dfs(i, j, k):
            if k == len(word):
                return True
            if (i < 0 or j < 0 or i >= col_num or j >= row_num or board[i][j] != word[k] or (i, j) in path):
                return False
            path.add((i, j))
            res = dfs(i - 1, j, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1)
            path.remove((i, j))
            return res

        for i in range(col_num):
            for j in range(row_num):
                if dfs(i, j, 0):
                    return True
        return False
