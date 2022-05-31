class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        
        if not head:
            return head
        prev = None
        current = head

        while left > 1:
            prev = current
            current = current.next
            left -= 1
            right -= 1
        
        end = prev
        rev = current

        while right > 0 and current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            right -= 1
        
        if end:
            end.next = prev
        else:
            head = prev
        rev.next = current
        return head
