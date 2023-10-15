# 0023 -  Merge k Sorted Lists

## Dates Reviewed
2023/10/15, 2023/09/14

## Problem Link

https://leetcode.com/problems/merge-k-sorted-lists/

## Approach : Recursive
Merge 2 adjacent lists at a time with a while loop until length of list is 1. Merging 2 linked lists with merge sort.


**Time Complexity**: $$O(k*log(n))$$
where k is average length of linked list and n is number of linked list.

**Space Complexity**: $$O(k*n)$$
where k is average length of linked list and n is number of linked list.

<TabItem value="python" label="Python">

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            res = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i != len(lists) -1 else None
                res.append(self.mergeTwoLists(list1, list2))
            lists = res
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        pointer = dummy
        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
        pointer.next = l1 or l2
        return dummy.next
```
</TabItem>
