# Problem link: https://leetcode.com/problems/combination-sum/
# Date: 2023/09/12
# Big-O: O(k^n) (k is target value and n is the length of candidates list)
# Overview:
#   - Recursive depth first search
#   - Base cases are when total sum (of elements in current array) > target and index out of bounds
#   - Keep adding elements to current array if base case not met
# <============ SOLUTION ============>

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def depth_first_search(cur, i, total):
            if total > target or i >= len(candidates):
                return
            if total == target:
                res.append(cur.copy())
                return

            cur.append(candidates[i])
            depth_first_search(cur, i, total + candidates[i])
            cur.pop()
            depth_first_search(cur, i + 1, total)

        depth_first_search([], 0, 0)

        return res
