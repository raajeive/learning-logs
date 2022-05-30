class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = lengthB = 0

        tempA = headA
        tempB = headB
        while tempA and tempB:
            lengthA += 1
            lengthB += 1
            tempA = tempA.next
            tempB = tempB.next
        if tempA:
            while tempA:
                lengthA += 1
                tempA = tempA.next
        else:
            while tempB:
                lengthB += 1
                tempB = tempB.next
        
        diff = abs(lengthA - lengthB)
        
        if lengthA > lengthB:
            while diff:
                headA = headA.next
                diff -= 1
        else:
            while diff:
                headB = headB.next
                diff -= 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
