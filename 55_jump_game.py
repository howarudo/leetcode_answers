# Problem link: https://leetcode.com/problems/jump-game/
# Date: 2023/09/14, 2023/10/01
# Big-O: O(n)
# Overview:
#   - Greed from behind, recursively change the "goal" of jumps
# <============ SOLUTION ============>

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
