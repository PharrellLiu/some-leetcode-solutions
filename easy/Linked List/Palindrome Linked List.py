class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        prev = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next
        prev.next = None
        dummy = None
        curr = slow
        while curr is not None:
            foll = curr.next
            curr.next = dummy
            dummy = curr
            curr = foll
        while dummy.val == head.val:
            dummy = dummy.next
            if dummy is None:
                return True
            head = head.next
        return False
