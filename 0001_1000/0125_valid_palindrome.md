# 0125 - Valid Palindrome

## Dates Reviewed
2023/12/18

## Problem Link

https://leetcode.com/problems/valid-palindrome/description/

## Approach : Simple

Remove prefix with replace. Then heckfor palindrome.

**Time Complexity**: $$O(n)$$
where n is the length of word

**Space Complexity**: $$O(1)$$
.

<TabItem value="python" label="Python">

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        special = "!@#$%^&*()_-=+\{\}:;\"\'<>,.\\/~` []?"
        s = s.lower()
        for c in special:
            s = s.replace(c, "")
        l, r = 0, len(s) - 1
        while l < r:
            if s[l]!= s[r]:
                return False
            l += 1
            r -= 1
        return True
```
</TabItem>
