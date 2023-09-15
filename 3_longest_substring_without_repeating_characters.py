# Problem link: https://leetcode.com/problems/longest-substring-without-repeating-characters
# Date: 2023/09/15
# Big-O: O(n)
# Overview:
#   - Two pointers, sliding window
#   - Fast pointer, r will increment one at a time
#   - When a repeated character is found, l will jump to the 1+ the location it was seen
# <============ SOLUTION ============>

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        l = 0
        for r in range(len(s)):
            if s[r] in seen.keys() and seen[s[r]] >= l:
                max_length = max(r - l, max_length)
                l = seen[s[r]] + 1
            seen[s[r]] = r
        max_length = max(len(s) - l, max_length)
        return max_length
