# Problem link: https://leetcode.com/problems/merge-k-sorted-lists/
# Date: 2023/09/14
# Big-O: O(klog(n)) where k is the average length of a list, and n is the number of lists
# Overview:
#   - Merge 2 adjacent lists at a time (wth mergeTwoLists function, binary merge sort)
#   - Then the merged_list will be the new lists and repeat merging process
#   - until there is only one list left
# <============ SOLUTION ============>

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
