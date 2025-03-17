class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        current = head
        prev = None
        head = head.next
        while current and current.next:
            adj = current.next
            if prev:
                prev.next = current.next
            current.next, adj.next = adj.next, current
            prev, current = current, current.next
        return head
            