# Problem link: https://leetcode.com/problems/climbing-stairs
# Date: 2023/09/14
# Big-O: O(n)
# Overview:
#   - Classic fibonacci recursive!
# <============ SOLUTION ============>

class Solution:
    def climbStairs(self, n: int) -> int:
        prev_2 = 0
        prev_1 = 1
        for _ in range(n):
            temp = prev_1
            prev_1 = prev_1 + prev_2
            prev_2 = temp
        return prev_1
