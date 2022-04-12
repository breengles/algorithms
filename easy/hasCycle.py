class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []  # O(n) in mem
        cur = head
        while cur is not None:
            visited.append(cur)
            cur = cur.next
            if cur in visited:
                return True

        return False

