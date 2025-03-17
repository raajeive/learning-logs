class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        result = list1
        
        firstpointer = lastpointer = list1
        
        for _ in range(b - a + 1):
            lastpointer = lastpointer.next
        
        for _ in range(a - 1):
            firstpointer = firstpointer.next
            lastpointer = lastpointer.next
        
        firstpointer.next = list2
        
        while list2.next:
            list2 = list2.next
        
        list2.next = lastpointer.next
        
        return result
