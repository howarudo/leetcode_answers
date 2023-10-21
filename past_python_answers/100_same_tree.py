# Problem link: https://leetcode.com/problems/same-tree/
# Date: 2023/09/16
# Big-O: O(n) (n is the number of nodes in total)
# Overview:
#   - depth first search
#   - check 4 possible cases
# <============ SOLUTION ============>

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return True
            if ((node1 is None) ^ (node2 is None)):
                return False
            if node1.val == node2.val:
                return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            return False
        return dfs(p, q)
