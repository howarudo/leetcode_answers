# 0217 - Contains Duplicate

## Dates Reviewed
2023/10/21

## Problem Link

https://leetcode.com/problems/contains-duplicate/description/

## Approach : Caching and for loop

Cache seen elements to a hash map and run a for loop. If element is found in hash map, return True.

**Time Complexity**: $$O(n)$$
where n is the number of elements in array

**Space Complexity**: $$O(n)$$
where n is the number of elements in array

<TabItem value="python" label="Python">

```python
# 2023/10/21 easy
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

```
</TabItem>
