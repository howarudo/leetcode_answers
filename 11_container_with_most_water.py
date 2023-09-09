# Problem link: https://leetcode.com/problems/container-with-most-water/
# Date: 2023/09/10
# Big-O: O(n)
# Overview:
#   - Closing window with 2 pointers
#   - Close inwards (l or r) depending on the height, pointless to close shorter height
# <============ SOLUTION ============>

class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(l, r):
            return (r-l) * min(height[l], height[r])
        l, r = 0, len(height)-1
        curr_area = area(l,r)
        while l < r:
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
            curr_area = max(area(l, r), curr_area)
        return curr_area
