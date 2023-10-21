# Problem link: https://leetcode.com/problems/search-in-rotated-sorted-array
# Date: 2023/09/15
# Big-O: O(log(n))
# Overview:
#   - Rotated sorted array could be seen as 2 sorted arrays
#   - Split a modified binary search into 2 cases (when mid is in the left sorted array or right)
#   - According to each case, increment l or decrement r
# <============ SOLUTION ============>

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # if mid in left sorted array
            if nums[mid] >= nums[0]:
                # if target in left
                if target >= nums[0] and nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target < nums[0] and nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
        return -1
