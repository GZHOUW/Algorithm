'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(None)
        prev = dummy
        prev.next = head
        cur = head
        while cur:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next
                
