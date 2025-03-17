class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        head = temp = None
        if list1.val < list2.val:
            head = list1
            temp = list1
            list1 = list1.next
        else:
            head = list2
            temp = list2
            list2 = list2.next
        
        while list1 and list2:
            if list1.val < list2.val:
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
        return head
