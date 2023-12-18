# 0036 - Valid Sudoku

## Dates Reviewed
2023/11/24, 2023/12/18

## Problem Link

https://leetcode.com/problems/valid-sudoku/description/

## Approach : Caching

Caching each number that appears on each row, column and sub-grid

**Time Complexity**: $$O(1)$$
(Technically O(1) because number of numbers in board is fixed.)
If number of board is not fixed, $$O(n)$$; where n is number of numbers

**Space Complexity**: $$O(1)$$
Same as time complexity

<TabItem value="python" label="Python">

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cache_grid = defaultdict(list)
        cache_row = defaultdict(list)
        cache_col = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if board[i][j] in cache_row[i] or board[i][j] in cache_grid[(i//3, j//3)] or board[i][j] in cache_col[j]:
                        return False
                    else:
                        cache_row[i].append(board[i][j])
                        cache_col[j].append(board[i][j])
                        cache_grid[(i//3, j//3)].append(board[i][j])
        return True
```
</TabItem>
