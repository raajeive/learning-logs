# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2

        if list2 == None:
            return list1
        
        result = temp = None

        if list1.val <= list2.val:
            result = list1
            temp = list1
            list1 = list1.next
        else:
            result = list2
            temp = list2
            list2 = list2.next

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            else:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
        
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        
        return result
