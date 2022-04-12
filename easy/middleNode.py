# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head  # 2 times faster than slow ==> when fast reaches the end slow will be at the middle

        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next

        return slow
