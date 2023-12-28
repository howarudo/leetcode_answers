# 0242 - Valid Anagram

## Dates Reviewed
2023/10/21, 2023/12/28

## Problem Link

https://leetcode.com/problems/valid-anagram/description/

## Approach : Caching one word into a hashmap

Cache one string into a hashmap. Run a for loop for the other string that checks if the key and values match with hashmap. To reduce time on checking if each key has 0 values, we remove the key once we know it is empty.

**Time Complexity**: $$O(n)$$
where n is the number of letters.

**Space Complexity**: $$O(n)$$
where n is the number of letters.

<TabItem value="python" label="Python">

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        goal = {}
        for letter in s:
            goal[letter] = goal.get(letter, 0) + 1
        for letter in t:
            goal_val = goal.get(letter, 0)
            if goal_val == 0:
                return False
            if goal_val == 1:
                goal.pop(letter)
            else:
                goal[letter] -= 1
        return len(goal) == 0
```
</TabItem>
