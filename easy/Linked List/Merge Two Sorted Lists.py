class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        head = ListNode(0)
        curr = head
        while l1 is not None or l2 is not None:
            if l1 is None and l2 is not None:
                curr.val = l2.val
                curr.next = l2.next
                break
            elif l2 is None and l1 is not None:
                curr.val = l1.val
                curr.next = l1.next
                break
            else:
                if l1.val > l2.val:
                    curr.val = l2.val
                    l2 = l2.next
                else:
                    curr.val = l1.val
                    l1 = l1.next
                curr.next = ListNode(0)
                curr = curr.next
        return head
