class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return head

        current = head
        
        while current:
            temp = Node(current.val)
            temp.next = current.next
            current.next = temp
            current = current.next.next
        
        current = head
        
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        newhead = head.next

        current = head
        copycurrent = Node(0)
        
        while current:
            copycurrent.next = current.next
            copycurrent = copycurrent.next
            current.next = copycurrent.next
            current = current.next
        
        return newhead
