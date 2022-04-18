from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            if q is None:
                return True
            else:
                return False
        elif q is None:
            return False

        pool = [(p, q)]

        while pool:
            for _ in range(len(pool)):
                node1, node2 = pool.pop(0)

                if node1.val != node2.val:
                    return False

                if node1.left is not None:
                    if node2.left is not None:
                        pool.append((node1.left, node2.left))
                    else:
                        return False
                elif node2.left is not None:
                    return False

                if node1.right is not None:
                    if node2.right is not None:
                        pool.append((node1.right, node2.right))
                    else:
                        return False
                elif node2.right is not None:
                    return False

        return True
