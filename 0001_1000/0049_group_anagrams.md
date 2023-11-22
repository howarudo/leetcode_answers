# 0049 - Group Anagrams

## Dates Reviewed
2023/11/22

## Problem Link

https://leetcode.com/problems/group-anagrams/description/

## Approach : Storing letters found as a hashmap key

Loop through each word, each letter combination in a word will have a unique key. Use this unique key to store the words in a hashmap

**Time Complexity**: $$O(n)$$
where n is the number of words

**Space Complexity**: $$O(n)$$
where n is the number of words

<TabItem value="python" label="Python">

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for l in s:
                key[ord(l) - ord('a')] += 1
            cache[tuple(key)].append(s)
        return cache.values()
```
</TabItem>
