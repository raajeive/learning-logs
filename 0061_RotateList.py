class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        k = k % count
        current = head
        for _ in range(k):
            current = current.next
            if not current:
                current = head
        
        temp = head
        while current.next:
            temp = temp.next
            current = current.next
        
        current.next = head
        head = temp.next
        temp.next = None
        
        return head

