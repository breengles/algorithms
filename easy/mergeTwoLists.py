from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2

        if cur1 is None:
            return cur2
        if cur2 is None:
            return cur1

        tmp = head = ListNode()  # simple trick that allows appending nodes, O(1) in mem

        while cur1 is not None and cur2 is not None:
            if cur1.val <= cur2.val:
                tmp.next, cur1 = cur1, cur1.next
            else:
                tmp.next, cur2 = cur2, cur2.next

            tmp = tmp.next

        if cur1 is not None:
            tmp.next = cur1
        else:
            tmp.next = cur2

        return head.next  # do not forget to move initial pointer to the actual value

