'''
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head): # recursion
        if not head or not head.next: # when the end of list is reached by recursion
            return head 
        
        next = head.next # head=4, next=5
        newHead = self.reverseList(next) # traverse all the way to end of list, newHead=5
        next.next = head # 5.next = 4,  5--->4
        head.next = None # 5-->4-->None
        
        return newHead
    
    def reverseList(self, head): # iteration
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
