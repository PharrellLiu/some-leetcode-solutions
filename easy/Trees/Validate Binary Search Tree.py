class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        if root is None or (root.left is None and root.right is None):
            return True
        inorder_list = inorder(root)
        i = 1
        length = len(inorder_list)
        while inorder_list[i] > inorder_list[i - 1]:
            i += 1
            if i == length:
                return True
        return False
