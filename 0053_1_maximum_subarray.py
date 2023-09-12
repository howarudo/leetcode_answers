# Problem link: https://leetcode.com/problems/maximum-subarray
# Date: 2023/09/13
# Big-O: O(n)
# Overview:
#   - Kadane's algorithm
#   - Traverses the whole array to find the max sum. Restarts summation when it becomes negative
#   - Divide and conquer is better
# <============ SOLUTION ============>

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
