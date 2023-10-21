# 0076 - Minimum Window Substring

## Dates Reviewed
2023/10/15, 2023/09/26

## Problem Link

https://leetcode.com/problems/minimum-window-substring/

## Approach : Sliding Window

Sliding window with 2 pointers. Store elements of goal in one hashmap. Fast pointers skim through until goal hashmap and window hashmap is equal. Then slow pointer moves until conditions are broken.

**Time Complexity**: $$O(n)$$
where n is the length of s

**Space Complexity**: $$O(n)$$
where n is the length of s

<TabItem value="python" label="Python">

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        current = {}
        min_str = s + "!"
        for i in t:
            window[i] = window.get(i, 0) + 1
        goal = len(window)
        counter = 0
        l = 0
        for r in range(len(s)):
            current[s[r]] = current.get(s[r], 0) + 1
            if s[r] in window and current[s[r]] == window[s[r]]:
                counter += 1
            while counter == goal:
                if len(min_str) > r - l:
                    min_str = s[l:r+1]
                if s[l] in window:
                    current[s[l]] -= 1
                    if window[s[l]] > current[s[l]]:
                        counter -= 1
                l += 1
        return "" if min_str == s + "!" else min_str
```
</TabItem>
