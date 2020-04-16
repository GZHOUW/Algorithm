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
    def reverseIter(self, head):
        res = None
        while head != None:
            temp = head # 1 2 3 4 5 None
            head = head.next # 2 3 4 5 None
            temp.next = res # temp = 1 None
            res = temp # temp = 1 None
        return res
    
    def reverseRecur(self, head):
        return
