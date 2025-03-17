class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        fastptr = head
        slowptr = head
        for _ in range(n):
            fastptr = fastptr.next
        if not fastptr:
            return head.next
        while fastptr and fastptr.next:
            fastptr = fastptr.next
            slowptr = slowptr.next
        slowptr.next = slowptr.next.next
        return head
