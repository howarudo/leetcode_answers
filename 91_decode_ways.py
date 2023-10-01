# Problem link: https://leetcode.com/problems/decode-ways/
# Date: 2023/10/01
# Big-O: O(n)
# Overview:
#   - cached dfs. base case is when it reaches end of string or is in cache
#   - Check if we could remove 1 element or 2 element for each dfs step
# <============ SOLUTION ============>

# 2023/10/01 REV OK
class Solution:
    def numDecodings(self, s: str) -> int:
        cached_dfs = {len(s): 1}

        def dfs(i):
            if i in cached_dfs:
                return cached_dfs[i]
            res = 0
            if s[i] != "0":
                res += dfs(i+1)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            cached_dfs[i] = res
            return res

        return dfs(0)
