class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head):
        group = 2
        
        tail = head
        
        while tail and tail.next:
            print(tail.val)
            previous, current = tail, tail.next
            count = 0

            while current and count < group:
                previous = current
                current = current.next
                count += 1

            if count % 2 == 0 :
                prev, cur = tail, tail.next

                while cur and count:
                    temp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = temp
                    count -= 1

                temp = tail.next
                tail.next = prev
                temp.next = cur
                tail = temp

            else:
                tail = previous
            
            group += 1
        
        return head
        
