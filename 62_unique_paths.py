# Problem link: https://leetcode.com/problems/unique-paths
# Date: 2023/09/14
# Big-O: O(m)
# Overview:
#   - Math!!!! Combinatorics!!!! It's (m+n-2) choose (m-1)
# <============ SOLUTION ============>

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # (m+n-2)C(m-1)
        if (m == 1 or n ==1):
            return 1

        N = m + n - 2
        for i in range(1, m - 1):
            print(N, n, m, i)
            N = N * (m + n - 2 - i)

        for i in range(1, m):
            print(N, n, m, i)
            N = N // i

        return N
