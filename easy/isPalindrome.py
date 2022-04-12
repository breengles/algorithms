# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # middle
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        prev = None
        cur = slow

        # reverse
        # it overwrites cur.next
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        # check
        start = head
        middle = prev
        while middle is not None:
            if start.val != middle.val:
                return False

            start = start.next
            middle = middle.next

        return True
