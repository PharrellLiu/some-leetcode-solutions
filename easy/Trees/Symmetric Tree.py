class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSymmetric2(l, r):
            if l is None and r is None:
                return True
            if l is not None and r is not None and l.val == r.val:
                return isSymmetric2(l.right, r.left) and isSymmetric2(l.left, r.right)
            return False

        if root is None:
            return True
        return isSymmetric2(root.left, root.right)
