# Problem link: https://leetcode.com/problems/longest-consecutive-sequence
# Date: 2023/09/21
# Big-O: O(n)
# Overview:
#   - Make a hashset of nums
#   - If we found an element that is the last element of a sequene, try to find how many other consecutives there are
#   - Then update longest
# <============ SOLUTION ============>

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest  = 0
        for num in nums:
            if num + 1 not in numsSet:
                curr_longest = 1
                while num - 1 in numsSet:
                    curr_longest += 1
                    num -= 1
                longest = max(curr_longest, longest)
        return longest
