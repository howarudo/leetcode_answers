# Problem link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Date: 2023/09/11
# Big-O: O(len(head))
# Overview:
#   - Use a dummy node before head
#   - l will be slow pointer, r is fast pointer. Let r move to the right n times
#   - Let l and r move until r hits a None (dead-end), then remove the node

# <============ SOLUTION ============>

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val = 0, next = head)
        l = dummy
        r = head
        while n > 0:
            r = r.next
            n -= 1
        while r:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next
