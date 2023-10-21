# Problem link: https://leetcode.com/problems/group-anagrams
# Date: 2023/09/17
# Big-O: O(m*n), m is the str length, n is the number of strs
# Overview:
#   - Use a hashmap of key = to ascii key - "a" ascii. This will group the anagrams together
#   - Run a loop to get all the elements on all strings
# <============ SOLUTION ============>

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen  = defaultdict(list)
        for i in range(len(strs)):
            key = [0] * 26
            for s in strs[i]:
                key[ord(s) - ord("a")] += 1
            seen[tuple(key)].append(strs[i])
        return seen.values()
