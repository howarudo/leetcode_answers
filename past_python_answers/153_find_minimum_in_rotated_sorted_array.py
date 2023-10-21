# Problem link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Date: 2023/09/30
# Big-O: O(log n)
# Overview:
#   - 2 pointers.
#   - Rotated array can be seen as 2 sorted arrays -> Use modified binary search
# <============ SOLUTION ============>

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[-1]:
                r = mid
            else:
                l = mid + 1
        return nums[(l+r)//2]
