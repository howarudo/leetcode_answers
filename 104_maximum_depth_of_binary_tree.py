# Problem link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Date: 2023/09/26
# Big-O: O(n)
# Overview:
#   - bfs. Use deque as a waiting list
# <============ SOLUTION ============>

# 2023/09/26 REV
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        count = 0
        while len(q) != 0:
            len_q = len(q)
            counted = False
            for _ in range(len_q):
                node = q.popleft()
                if node:
                    if not counted:
                        count += 1
                        counted = True
                    q.append(node.left)
                    q.append(node.right)
        return count
