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


# Merge Two Sorted Lists
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None and l2 is None:
        return None
    head = ListNode(0)
    curr = head
    while l1 is not None or l2 is not None:
        if l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.val = l1.val
                l1 = l1.next
            else:
                curr.val = l2.val
                l2 = l2.next
            curr.next = ListNode(0)
            curr = curr.next
        elif l1 is None and l2 is not None:
            curr.val = l2.val
            curr.next = l2.next
            break
        elif l1 is not None and l2 is None:
            curr.val = l1.val
            curr.next = l1.next
            break
    return head


# Palindrome Linked List
def isPalindrome(self, head: ListNode) -> bool:
    if head is None:
        return True
    if head.next is None:
        return True
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    if fast is not None:
        slow = slow.next

    def reverse(root):
        prev = None
        curr = root
        furt = curr.next
        while True:
            curr.next = prev
            prev = curr
            curr = furt
            if curr is None:
                return prev
            else:
                furt = curr.next

    newHead = reverse(slow)
    while newHead is not None:
        if newHead.val != head.val:
            return False
        newHead = newHead.next
        head = head.next
    return True


# Linked List Cycle
def hasCycle(self, head: ListNode) -> bool:
    if head is None:
        return None
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        fast = fast.next.next
        slow = slow.next
    return True
