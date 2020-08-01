from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        nodes_list1 = [root]
        nodes_list2 = []
        while len(nodes_list1) != 0:
            nodes_val = []
            for i in nodes_list1:
                nodes_val.append(i.val)
                if i.left is not None:
                    nodes_list2.append(i.left)
                if i.right is not None:
                    nodes_list2.append(i.right)
            nodes_list1 = nodes_list2
            nodes_list2 = []
            result.append(nodes_val)
        return result
