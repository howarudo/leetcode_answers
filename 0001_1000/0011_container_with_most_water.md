# 0011 - Container With Most Water

## Dates Reviewed
2023/10/21, 2023/12/29

## Problem Link

https://leetcode.com/problems/container-with-most-water/description

## Approach : Closing window

Classic closing window problem

**Time Complexity**: $$O(n)$$
where n is the number of elements in the array

**Space Complexity**: $$O(1)$$

<TabItem value="python" label="Python">

```python
# 2023/10/21
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(l, r):
            return min(height[l], height[r]) * (r -l)
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, area(l, r))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
```
</TabItem>
