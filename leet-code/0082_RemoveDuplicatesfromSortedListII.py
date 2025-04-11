# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        temp = returnHead = None
        while head and head.next:
            if head.val != head.next.val:
                if not temp:
                    temp = returnHead = head
                    head = head.next
                    temp.next = None
                else:
                    temp.next = head
                    temp = temp.next
                    head = head.next
                    temp.next = None
            else:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
        if head and temp:
            temp.next = head
            temp = temp.next
            temp.next = None
        if not temp:
            return head
        return returnHead
