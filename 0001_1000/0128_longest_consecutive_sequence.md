# 0128 - Longest Consecutive Sequence

## Dates Reviewed
2023/11/24, 2023/12/28

## Problem Link

https://leetcode.com/problems/longest-consecutive-sequence/description/

## Approach : Caching

Caching all number to a hashmap. For every number check if it is the last of a sequnce and loop through the possible sequences. At this point, because we are using a hashmap, the time complexity of looking at numbers for possible sequences will be $$O(1)$$.

**Time Complexity**: $$O(n)$$
where n is the number of numbers in nums

**Space Complexity**: $$O(n)$$
where n is the number of numbers in nums

<TabItem value="python" label="Python">

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        for num in nums:
            if num + 1 not in nums_set:
                count = 1
                while num - count in nums_set:
                    count += 1
                max_count = max(count, max_count)
        return max_count

```
</TabItem>
