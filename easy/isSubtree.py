from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, root, subroot):
        if not root and not subroot:
            return True  # empty nodes

        if (root and not subroot) or (not root and subroot):
            return False  # unmatched structure

        if root.val != subroot.val:
            return False  # not equal vals in roots ==> no need to check deeper

        return self.check(root.left, subroot.left) and self.check(root.right, subroot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:  # empty subtree cannot contain subRoot
            return False

        if root.val == subRoot.val and self.check(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

