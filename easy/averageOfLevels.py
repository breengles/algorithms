# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        bfs = [root]
        res = []
        while len(bfs) > 0:
            s = 0
            n = len(bfs)
            for _ in range(n):  # we have `n` nodes on the current level
                node = bfs.pop(0)  # get first elem in list
                s += node.val

                if node.left is not None:
                    bfs.append(node.left)  # append to the end i.e. to the right
                if node.right is not None:
                    bfs.append(node.right)

            res.append(s / n)

        return res

