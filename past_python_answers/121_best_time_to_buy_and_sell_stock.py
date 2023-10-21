# Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Date: 2023/09/19
# Big-O: O(n), where n is the length of the array
# Overview:
#   - 2 pointers. Fast pointer in for loop
#   - Slow pointer will catch up to fast pointer when a lower price is found
# <============ SOLUTION ============>

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        curr_max = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                curr_max = max(curr_max, prices[r] - prices[l])
        return curr_max
