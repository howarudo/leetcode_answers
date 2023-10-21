# Problem link: https://leetcode.com/problems/valid-palindrome
# Date: 2023/09/19
# Big-O: O(n)
# Overview:
#   - Remove special characters with for loop, then lower with lower()
#   - Check for palindrome with while loop (closing window)
# <============ SOLUTION ============>

class Solution:
    def isPalindrome(self, s: str) -> bool:
        special_char = ":.,@#$%^&*_'\\\"\{\}[]-?;/<>~`!() "
        for spec in special_char:
            s = s.replace(spec, "")
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
