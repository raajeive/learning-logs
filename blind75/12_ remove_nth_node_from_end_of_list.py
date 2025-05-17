# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        if n == 0:
            return head

        head1, head2 = head, head

        while n > 0:
            head1 = head1.next
            n -= 1

        if n > 0:
            return head
        
        if head1 == None:
            return head.next

        while head1.next != None:
            head1 = head1.next
            head2 = head2.next

        head2.next = head2.next.next 

        return head
