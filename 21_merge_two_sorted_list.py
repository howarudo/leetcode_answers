# Problem link: https://leetcode.com/problems/merge-two-sorted-lists
# Date: 2023/09/12
# Big-O: O(n) (n is the sum of lengths of list1 and list2)
# Overview:
#   - Merge operation of merge sort
#   - Holder for answer and a pointer that points to whichever element is smaller
# <============ SOLUTION ============>

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        holder = ListNode()
        pointer = holder
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        pointer.next = list1 or list2
        return holder.next
