/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

https://leetcode.com/problems/add-two-numbers/
 */

#include <stdio.h>

 struct ListNode {
     int val;
     struct ListNode *next;
 };

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode * head = NULL;
    struct ListNode * current = NULL;
    int rem = 0;
    while(l1 != NULL || l2 != NULL){
        struct ListNode * temp = (struct ListNode *)(malloc(sizeof(struct ListNode)));
        if (l1 && l2){
            temp->val = l1->val + l2->val + rem;
        }
        else if (l1){
            temp->val = l1->val + rem;
        }
        else{
            temp->val = l2->val + rem;
        }
        if(temp->val >= 10){
            rem = temp->val / 10;
            temp->val = temp->val % 10;
        }
        else{
            rem = 0;
        }
        temp->next = NULL;
        if(!head){
            head = temp;
            current = temp;
        }
        else{
            current->next = temp;
            current = current->next;
        }
        if(l1){
            l1 = l1->next;
        }
        if(l2){
           l2 = l2->next; 
        }
    }
    if(rem){
        struct ListNode * temp = (struct ListNode *)malloc(sizeof(struct ListNode));
        temp->val = rem;
        temp->next = NULL;
        current->next = temp;
        current = current->next;
    }
    return head;

}
