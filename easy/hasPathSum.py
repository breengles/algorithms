from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return 0

        dfs = [(root, root.val)]

        while dfs:
            for _ in range(len(dfs)):
                node, s = dfs.pop(-1)

                if node.left is None and node.right is None:
                    if s == targetSum:
                        return True

                if node.left is not None:
                    dfs.append((node.left, s + node.left.val))
                if node.right is not None:
                    dfs.append((node.right, s + node.right.val))

        return False

