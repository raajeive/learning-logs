# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):

        if head == None or head.next == None or head.next.next == None:
            return
        
        fast = head
        slow = head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        
        # split the list
        head2 = slow.next
        slow.next = None

        # reverse the second half
        prev = None
        while head2:
            temp = head2
            head2 = head2.next
            temp.next = prev
            prev = temp
        
        head2 = prev

        start = head
        while start != None and head2 != None:
            temp = start.next
            start.next = head2
            head2 = head2.next
            start.next.next = temp
            start = start.next.next
    