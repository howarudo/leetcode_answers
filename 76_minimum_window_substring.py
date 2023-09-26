# Problem link: https://leetcode.com/problems/minimum-window-substring/description/
# Date: 2023/09/26
# Big-O: O(n)
# Overview:
#   - Two pointers, sliding window algorithm.
#   - Window and target hashmap as storage
#   - While window satisfies target, move increment left pointer until does not. Then increment right pointer
# <============ SOLUTION ============>

# REV 2023/09/26
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, target = {}, {}

        for e in t:
            target[e] = target.get(e, 0) + 1

        l = 0
        count, goal = 0, len(target.keys())
        min_str = s + "!"

        for r in range(len(s)):
            letter = s[r]
            if letter in target:
                window[letter] = window.get(letter, 0) + 1
                if window[letter] == target[letter]:
                    count += 1
                while count == goal:
                    if len(min_str) > r - l + 1:
                        min_str = s[l:r+1]
                    if s[l] in target:
                        window[s[l]] -= 1
                        if window[s[l]] < target[s[l]]:
                            count -= 1
                    l += 1

        return "" if min_str == s + "!" else min_str
