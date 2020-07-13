'''
Write a program to find the node at which the intersection of two singly linked lists begins.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        # find the length of both lists
        a = headA
        b = headB
        aLen = 0
        bLen = 0
        
        while a:
            a = a.next
            aLen += 1
        while b:
            b = b.next
            bLen += 1
        
        # find the difference in length
        d = abs(aLen-bLen)
        
        a = headA
        b = headB
        
        # omit the first d nodes of the longer list
        while aLen > bLen:
            a = a.next
            aLen -= 1
        while bLen > aLen:
            b = b.next
            bLen -= 1
        
        # start from a and b and compare cur node
        while a and b:
            if a == b:
                return a # or b
            else:
                a = a.next
                b = b.next
        return None # no intersection found
