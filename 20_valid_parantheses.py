# Problem link: https://leetcode.com/problems/valid-parentheses/
# Date: 2023/09/11
# Big-O: O(n)
# Overview:
#   - bracket_dict correlates the beginning and ending of a bracket
#   - Take a for loop of s,
#   - Notice that the if the latest opening bracket is "(", the next element has to be another opening bracket
#   - or a ")". If the string does not satisfy this, we return a False
# <============ SOLUTION ============>

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"(":")", "{": "}", "[":"]"}
        order = []
        for brac in s:
            if brac in bracket_dict.keys():
                order.append(bracket_dict[brac])
            else:
                if len(order) == 0 or order[-1] != brac:
                    return False
                else:
                    order.pop()
        return len(order) == 0
