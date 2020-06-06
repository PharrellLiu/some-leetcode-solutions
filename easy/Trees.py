from typing import List

"""Tree problems can be solved either breadth-first or depth-first."""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Maximum Depth of Binary Tree
def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Validate Binary Search Tree
def isValidBST(self, root: TreeNode) -> bool:
    def inOrder(root):
        if root is None:
            return []
        return inOrder(root.left) + [root.val] + inOrder(root.right)

    values = inOrder(root)
    i = 0
    while i < len(values) - 1:
        if values[i] >= values[i + 1]:
            return False
        i += 1
    return True


# Symmetric Tree
def isSymmetric(self, root: TreeNode) -> bool:
    if root is None:
        return True

    def judge(l, r):
        if (l is None and r is not None) or (l is not None and r is None):
            return False
        if l is None and r is None:
            return True
        return (l.val == r.val) and judge(l.right, r.left) and judge(l.left, r.right)

    return judge(root.left, root.right)


# Binary Tree Level Order Traversal
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
        return []
    ans = []
    queue = [root]
    queueNext = []
    while len(queue) != 0:
        res = []
        for i in queue:
            res.append(i.val)
            if i.left is not None:
                queueNext.append(i.left)
            if i.right is not None:
                queueNext.append(i.right)
        queue.clear()
        queue = queueNext[:]
        queueNext.clear()
        ans.append(res)
    return ans


# Convert Sorted Array to Binary Search Tree
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if len(nums) == 0:
        return None

    def buildBST(l, r):
        if l > r:
            return None
        mid = l + (r - l) // 2
        root = TreeNode(nums[mid])
        root.left = buildBST(l, mid - 1)
        root.right = buildBST(mid + 1, r)
        return root

    return buildBST(0, len(nums) - 1)
