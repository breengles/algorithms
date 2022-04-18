from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        dfs = [(root, 1)]
        max_depth = 1
        while len(dfs) > 0:
            for _ in range(len(dfs)):
                node, cur_depth = dfs.pop(-1)
                max_depth = max(max_depth, cur_depth)

                if node.left is not None:
                    dfs.append((node.left, cur_depth + 1))
                if node.right is not None:
                    dfs.append((node.right, cur_depth + 1))

        return max_depth
