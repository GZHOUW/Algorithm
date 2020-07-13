'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
  Given this linked list: 1->2->3->4->5
  For k = 2, you should return: 2->1->4->3->5
  For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        p = head
        length = 0
        while p:
            length += 1
            p = p.next
        
        idx = 1
        while idx+k-1 <= length:
            head = self.reverseBetween(head, idx, idx+k-1)
            idx += k
        
        return head
    
    def reverseBetween(self, head, m, n):
        if not head:
            return head
        
        cur = head # main pointer
        prev = None # always 1 before cur
        
        # Move cur to m position and prev to one before
        for _ in range(m-1): # runs once for m=2
            prev = cur
            cur = cur.next
        
        mNode = cur # the node at m, will be connected to n+1 node
        mPrev = prev # the node before m node
        
        for _ in range(m, n+1):
            nex = cur.next # points at one after cur
            cur.next = prev # connect cur with previous element == reverse
            
            # move prev and cur one step forward for next iteration
            prev = cur
            cur = nex
        
        # At this point, 1:n are correctly reversed, but not connected with n+1:end
        # e.g. prev = 4->3->2->1    cur = 5->6->None
        if mPrev:
            mPrev.next = prev
        else: # nPrev is None --> reverse only the first node
            head = prev
        mNode.next =  cur
        
        return head
