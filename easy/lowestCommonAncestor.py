# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_depth(self, root, target):
        dfs = [(root, 1)]
        while dfs:
            for _ in range(len(dfs)):
                node, depth = dfs.pop(-1)
                if node.val == target.val:
                    return depth

                if node.left:
                    node.left.parent = node
                    dfs.append((node.left, depth + 1))
                if node.right:
                    node.right.parent = node
                    dfs.append((node.right, depth + 1))

    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        p_depth = self.get_depth(root, p)
        q_depth = self.get_depth(root, q)

        while p.val != q.val:
            if p_depth > q_depth:
                p = p.parent
                p_depth -= 1
            elif q_depth > p_depth:
                q = q.parent
                q_depth -= 1
            else:
                p = p.parent
                q = q.parent

        return p

