class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        if not head and not head.next:
            return head

        current, previous = head, None
        
        while current:
            cur = current
            count = k
            while count and cur:
                cur = cur.next
                count -= 1

            if not count:
                start = previous.next if previous else head
                prev = previous
                
                while start and count < k:
                    temp = start.next
                    start.next = prev
                    prev = start
                    start = temp
                    count += 1
                
                if previous:
                    previous.next = prev
                else:
                    head = prev
                current.next = start
            previous = current
            current = cur
        
        return head

