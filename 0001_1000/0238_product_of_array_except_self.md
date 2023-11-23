# 0238 - Product of Array Except Self

## Dates Reviewed
2023/11/23

## Problem Link

https://leetcode.com/problems/product-of-array-except-self/description/

## Approach : Caching product of previous and next numbers
Cache previous numbers' product in prefix and after in postfix. The result wll be product of prefix and postfix

**Time Complexity**: $$O(n)$$
where n is the number of numbers

**Space Complexity**: $$O(n)$$
where n is the number of numbers

<TabItem value="python" label="Python">

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        curr_prefix = 1
        curr_postfix = 1
        for num in nums:
            prefix.append(curr_prefix)
            curr_prefix *= num
        for i in range(len(nums)-1, -1, -1):
            postfix.append(curr_postfix)
            curr_postfix *= nums[i]
        res = []
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[len(nums)-1-i])
        return res
```
</TabItem>
