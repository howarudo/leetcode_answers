# Problem link: https://leetcode.com/problems/validate-binary-search-tree
# Date: 2023/09/16
# Big-O: O(2^n)
# Overview:
#   - depth first search
#   - cache lmax and rmin for condition checking
# <============ SOLUTION ============>

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lmax, rmin):
            if node is None:
                return True
            lNode = node.left
            rNode = node.right
            if node.val >= lmax or node.val <= rmin:
                return False
            res = dfs(lNode, min(lmax, node.val), rmin) and dfs(rNode, lmax, max(rmin, node.val))
            return res

        return dfs(root, float("infinity"), -1 * float("infinity"))
