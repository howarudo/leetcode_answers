# Problem link: https://leetcode.com/problems/number-of-1-bits
# Date: 2023/09/30
# Big-O: O(1)
# Overview:
#   - Shift n by i, and check last digit if its 1
#   - If 1, increment counter
#   -
# <============ SOLUTION ============>

# 2023/09/30 ez first try
class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for i in range(32):
            if (n >> i) & 1 == 1:
                counter += 1
        return counter
