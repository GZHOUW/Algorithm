'''
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
  Input: 1->2->3->4->5->NULL, m = 2, n = 4
  Output: 1->4->3->2->5->NULL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
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
