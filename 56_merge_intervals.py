# Problem link: https://leetcode.com/problems/merge-intervals/
# Date: 2023/09/14
# Big-O: O(nlog(n))
# Overview:
#   - Sort the intervals with the first element
#   - Now, we can use the last element and the adjacent list's first element to check for overlap
#   - Update lastInterval whenever there is an overlap. If no more overlap, append
# <============ SOLUTION ============>

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        lastInterval = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if lastInterval[1] >= intervals[i][0]:
                lastInterval = [lastInterval[0], max(intervals[i][1], lastInterval[1])]
            else:
                res.append(lastInterval)
                lastInterval = intervals[i]
        res.append(lastInterval)
        return res
