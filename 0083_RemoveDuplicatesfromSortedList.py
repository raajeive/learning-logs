class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        
        previous = head
        
        current = head.next
        
        while current:
            if current.val == previous.val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
        
        return head

