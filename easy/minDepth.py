# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_leaf(self, node):
        return node.left is None and node.right is None

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        bfs = [root]

        depth = 0
        while len(bfs) > 0:
            depth += 1
            n = len(bfs)

            for _ in range(n):
                node = bfs.pop(0)

                if self.is_leaf(node):
                    return depth

                if node.left is not None:
                    bfs.append(node.left)
                if node.right is not None:
                    bfs.append(node.right)

