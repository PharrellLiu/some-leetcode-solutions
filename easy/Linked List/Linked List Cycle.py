class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None:
                return False
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
        return True
