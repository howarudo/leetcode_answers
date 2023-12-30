# 0020 - Valid Parantheses

## Dates Reviewed
2023/12/30

## Problem Link

https://leetcode.com/problems/valid-parentheses/description/

## Approach : Stack

Trick is that if a closing bracket appears, the bracket before that must be it's opening bracket.
Use a stack to monitor the opening brackets. When a closing bracket is found, check if the last element in stack is it's opening bracket.

**Time Complexity**: $$O(n)$$
where n is the number of brackets

**Space Complexity**: $$O(1)$$

<TabItem value="python" label="Python">

```python
# 2023/12/30
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = deque()
        brackets = {"}": "{", ")": "(", "]": "["}
        for b in s:
            if b in brackets:
                if len(bracket_stack) == 0:
                    return False
                if bracket_stack.pop() != brackets[b]:
                    return False
            else:
                bracket_stack.append(b)
        return len(bracket_stack) == 0

```
</TabItem>
