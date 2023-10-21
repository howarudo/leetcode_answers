# 0033 - Search in Rotated Sorted Array

## Dates Reviewed
2023/10/21, 2023/09/27

## Problem Link

https://leetcode.com/problems/search-in-rotated-sorted-array/description/

## Approach : Binary search

Use a binary search-like method with more cases. A rotated sorted array could be seen as two sorted arrays -> We just have to adjust the original binary search to fit more cases.

**Time Complexity**: $$O(log * n)$$
where n is the number of elements in the sorted array

**Space Complexity**: $$O(1)$$

<TabItem value="python" label="Python">

```python
# 2023/10/21
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0]:
                if target >= nums[0] and target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target < nums[0] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
        return (l+r)//2 if nums[(l+r)//2] == target else -1
```
</TabItem>
