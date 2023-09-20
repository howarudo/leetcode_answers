# Problem link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Date: 2023/09/20
# Big-O: O(n)
# Overview:
#   - dfs
#   - For every node, check the max path of l and r, then check if this is better than global value
#   - But return only the max path of l and r (without going through root)
# <============ SOLUTION ============>

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            left_dfs = max(dfs(node.left), 0)
            right_dfs = max(dfs(node.right), 0)
            if left_dfs + right_dfs + node.val > res[0]:
                res[0] = left_dfs + right_dfs + node.val
            return max(left_dfs, right_dfs) + node.val
        dfs(root)
        return res[0]
