# 0104 - Maximum Depth Of Binary Tree

## Dates Reviewed
2023/10/15, 2023/09/26

## Problem Link

https://leetcode.com/problems/maximum-depth-of-binary-tree/

## Approach : Breadth First Search

Breadth first search. Use deque as a 'waiting list' for nodes. Once we clear one layer of nodes, increment counter.

**Time Complexity**: $$O(n)$$
where n is the number of nodes.

**Space Complexity**: $$O(n)$$
where n is the number of nodes.

<TabItem value="python" label="Python">

```python
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
```
</TabItem>
