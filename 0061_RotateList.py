class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        current = head
        count = 1
        while current.next:
            count += 1
            current = current.next
        current.next = head

        k = k % count
        current = head
        for _ in range(count - k - 1):
            current = current.next

        head = current.next
        current.next = None
        
        return head

