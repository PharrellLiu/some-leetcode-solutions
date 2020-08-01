from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def arrayToBST(l, r):
            if l > r:
                return None
            mid = l + (r - l) // 2
            node = TreeNode(nums[mid])
            node.left = arrayToBST(l, mid - 1)
            node.right = arrayToBST(mid + 1, r)
            return node

        return arrayToBST(0, len(nums) - 1)
