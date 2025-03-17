class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head):
        
        fast = slow = head
        
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        current = slow.next
        end = None
        while current:
            temp = current.next
            current.next = end
            end = current
            current = temp
        
        slow.next = end
        
        maxvalue = 0
        slow = slow.next
        while slow:
            maxvalue = max(maxvalue, head.val + slow.val)
            head = head.next
            slow = slow.next
        
        return maxvalue
