# 0167 - Two Sum II

## Dates Reviewed
2023/12/28

## Problem Link

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Approach : Closing window

Since the array is sorted, just use a closing window to check until the sum is equal to the target.

**Time Complexity**: $$O(n)$$
where n is the number of numbers in array

**Space Complexity**: $$O(1)$$
did not use any extra memory

<TabItem value="python" label="Python">

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l+1, r+1]
            if curr_sum < target:
                l += 1
            else:
                r -= 1

```
</TabItem>
