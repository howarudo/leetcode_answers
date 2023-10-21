# Problem link: https://leetcode.com/problems/reverse-bits/
# Date: 2023/09/30
# Big-O: O(1)
# Overview:
#   - Use python libraries and we done!
#   -
#   -
# <============ SOLUTION ============>

# 2023/09/30 first try
class Solution:
    def reverseBits(self, n: int) -> int:
        n_str = '{:032b}'.format(n)
        reversed_n = n_str[::-1]
        return int(reversed_n, 2)
