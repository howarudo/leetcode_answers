# 0347 - Top K Frequent Elements


## Dates Reviewed
2023/11/23

## Problem Link

https://leetcode.com/problems/top-k-frequent-elements/description/

## Approach : Caching

Have a cache to store values and number, then have an array where the index of array represents frequency and element is an array of numbers.

**Time Complexity**: $$O(n)$$
where n is the number of numbers

**Space Complexity**: $$O(n)$$
where n is the number of numbers

<TabItem value="python" label="Python">

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        rank = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            cache[num] = cache.get(num, 0) + 1
        for key, value in cache.items():
            rank[value].append(key)
        res = []
        for i in range(len(rank)-1, -1, -1):
            for num in rank[i]:
                res.append(num)
                if len(res) == k:
                    return res
```
</TabItem>
