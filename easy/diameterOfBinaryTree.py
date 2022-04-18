from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def calc_diameter(self, root):
        if root is None:
            # leaf ==> empty subtree ==> diameter == 0, height == 0
            return 0, 0

        left_d, left_h = self.calc_diameter(root.left)
        right_d, right_h = self.calc_diameter(root.right)
        cur_h = max(left_h, right_h) + 1

        # max diameter either pass through root ==> it is heights of left and rights subtrees
        # or diameter of left
        # or diameter of right
        return max(left_d, right_d, left_h + right_h), cur_h

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.calc_diameter(root)[0]

