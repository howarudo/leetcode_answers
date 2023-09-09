# Problem link: https://leetcode.com/problems/3sum/
# Date: 2023/09/10
# Big-O: n^2 (for loop is n, closing window (n) per loop)
# Overview:
#   - Okay to sort (log n) the nums bcs solution is going to be n^2 anyway
#   - Closing window depending on sum <>= 0
#   - Skip equivalent l and r pointers
# <============ SOLUTION ============>

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    # We skip repeated l and r first before incrementing because we are comparing
                    # with the current pointers
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans
