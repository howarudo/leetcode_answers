# 0042 - Trapping rain water

## Dates Reviewed
2023/12/29

## Problem Link

https://leetcode.com/problems/trapping-rain-water/description/

## Approach : two pointer greedy

Use a two-pointer approach to iterate the array of heights whle maintaining start and end of the array. At each step, move the smaller pointer and take the maximum. Cumulate the total area by adding `min(max_left, max_right) - current_height`.

**Time Complexity**: $$O(n)$$
where n is the number of ...

**Space Complexity**: $$O(1)$$


<TabItem value="python" label="Python">

```python
# 2023/12/29
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        area = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                area += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                area += right_max - height[r]
        return area

```
</TabItem>
