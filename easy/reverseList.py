# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 -> 2 -> 3
        1 <- 2 <- 3
        """
        prev = None
        cur = head

        while cur is not None:
            cur.next, prev, cur = prev, cur, cur.next

        return prev
