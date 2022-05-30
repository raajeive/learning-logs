class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """

        """
        find the mid
        """

        fast = slow = head        
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow
        slow = slow.next
        mid.next = None

        """
        reverse the second half of the list
        """

        prev = temp = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        """
        merge both list
        """
        temp = head
        while head and prev:
            head = head.next
            
            temp.next = prev
            prev = prev.next
            temp = temp.next
            
            temp.next = head
            temp = temp.next
