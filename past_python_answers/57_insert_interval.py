# Problem link: https://leetcode.com/problems/insert-interval/
# Date: 2023/09/19, 2023/10/01
# Big-O: O(n), n is the length of intervals
# Overview:
#   - For each element in intervals, there are 3 cases to be considered
#   - newInterval < rest of elements, newInterval > rest of elements, and newInterval has to be merged with current element
#   - For first, we could return it immediately bcs there no merge is required. For second, we could only append and merge later. For third, we can renew newInterval
# <============ SOLUTION ============>

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            print(newInterval, intervals[i])
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res
