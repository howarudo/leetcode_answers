# Problem link: https://leetcode.com/problems/house-robber/description/
# Date: 2023/09/30
# Big-O: O(n)
# Overview:
#   - cached dfs.
#   - Base cases are when it reaches the end, or last element
#   - Draw a tree diagram + what to cache. sometimes you dont have to pass curr_sum to dfs
# <============ SOLUTION ============>

# 2023/09/30 firs try
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache_dfs = {}
        def dfs(i):
            if i in cache_dfs:
                return cache_dfs[i]
            if i == len(nums) - 1:
                cache_dfs[i] = nums[i]
                return nums[i]
            if i == len(nums):
                cache_dfs[i] = 0
                return 0
            max_sum = max(dfs(i+2) + nums[i], dfs(i+1))
            cache_dfs[i] = max_sum
            return max_sum
        return dfs(0)
