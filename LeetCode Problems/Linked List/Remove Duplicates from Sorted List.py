'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def deleteDuplicates(self, head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val: 
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            return head.next
        else:
            return head
