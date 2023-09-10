# Problem link: https://leetcode.com/problems/longest-palindromic-substring
# Date: 2023/09/10
# Big-O: O(n^2)
# Overview:
#   - There are 2 types of palindromes. Odd: "bab", "adbda" or Even: "", "aa"
#   - Given a center, ("" when even, "x" when odd), palidromeSearcher looks for the longest palindrome
#   - Run a for loop for each center!
# <============ SOLUTION ============>

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindromeSearcher(curr:str, l: int, r: int) -> str:
            while l>=0 and r<len(s) and s[l] == s[r]:
                curr = s[l] + curr + s[r]
                l -= 1
                r += 1
            return curr

        curr_max = ""
        for i in range(2*len(s)+1):
            if i%2 == 0:
                l, r = int(i/2), int(i/2+1)
                curr = ""
            else:
                l, r = int((i-1)/2-1), int((i+1)/2)
                curr = s[int((i-1)/2)]
            curr_palindrome = palindromeSearcher(curr, l, r)
            if len(curr_palindrome) > len(curr_max):
                curr_max = curr_palindrome
        return curr_max
