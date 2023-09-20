# Problem link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# Date: 2023/09/20
# Big-O: O(n)
# Overview:
#   - dfs.
#   - Key: understand that knowing the index of the root on inorder will tell us the next preorder and inorder's array
#   - Then do a recursion
# <============ SOLUTION ============>

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = preorder[0]
        mid = inorder.index(root)
        node = TreeNode(val=root, left=self.buildTree(preorder[1:mid+1], inorder[:mid]), right=self.buildTree(preorder[mid+1:], inorder[mid + 1:]))
        return node
