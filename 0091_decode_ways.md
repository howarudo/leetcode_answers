# 0091 - Decode Ways

## Dates Reviewed
2023/10/21, 2023/10/01

## Problem Link

https://leetcode.com/problems/decode-ways/description/

## Approach : Depth first search

Depth first search on the message's removing first letter and first 2 letters. Base case met when
1. The string is found previously on cache or
2. If we reach end of string or
3. String starts with `0`

**Time Complexity**: $$O(n)$$
where n is the length of string. This is achieved because of using cache.

**Space Complexity**: $$O(n)$$
where n is the length of string.

<TabItem value="python" label="Python">

```python
# 2023/10/21 REV OK
class Solution:
    def numDecodings(self, s: str) -> int:
        cache_dfs = {"": 1}
        def dfs(s):
            if s in cache_dfs:
                return cache_dfs[s]
            if s[0] == "0":
                return 0
            ans = dfs(s[1:])
            if len(s) > 1 and (s[0] == "1" or (s[0] == "2" and s[1] in "0123456")):
                ans += dfs(s[2:])
            cache_dfs[s] = ans
            return ans
        return dfs(s)
```
</TabItem>
