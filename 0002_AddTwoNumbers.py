class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = None
        temp = None
        carry = 0
        while(l1 or l2):
            newNode = ListNode()
            newNode.val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if newNode.val > 9:
                carry = 1
                newNode.val = newNode.val % 10
            else:
                carry = 0
            newNode.next = None
            if temp:
                temp.next = newNode
                temp = temp.next
            if not result:
                result = newNode
                temp = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry != 0:
            newNode = ListNode()
            newNode.val = carry
            newNode.next = None
            temp.next = newNode

        return result
