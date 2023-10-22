# 0001 - Two Sum

## Dates Reviewed
2023/10/23

## Problem Link

https://leetcode.com/problems/two-sum/description/

## Approach : For loop with hashmap

Cache seen values in hashmap such that when we find the other pair (that sums to target), we will return the pair. This will make the complexity `O(n)` instead of the brute force with complexity `O(n^2)`

**Time Complexity**: $$O(n)$$
where n is the number of elements in nums

**Space Complexity**: $$O(n)$$
where n is the number of elements in nums

<TabItem value="python" label="Python">

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            if target - nums[i] in cache:
                return [i, cache[target-nums[i]]]
            cache[nums[i]] = i
```
</TabItem>
