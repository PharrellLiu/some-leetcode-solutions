"""Do not forget the Two-pointer technique, which not only applicable to Array problems but also Linked List problems
as well. Another technique to greatly simplify coding in linked list problems is the dummy node trick."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Delete Node in a Linked List
def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next


# Remove Nth Node From End of List
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    fast = head
    slow = head
    for i in range(n):
        fast = fast.next
    if fast is None:
        return head.next
    while fast is not None and fast.next is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head


# Reverse Linked List
def reverseList(self, head: ListNode) -> ListNode:
    if head is None:
        return head
    prev = None
    curr = head
    furt = curr.next
    while True:
        curr.next = prev
        prev = curr
        curr = furt
        if curr is None:
            return prev
        else:
            furt = curr.next
