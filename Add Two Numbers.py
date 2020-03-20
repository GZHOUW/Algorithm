'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1 = l1
        int1 = ''
        while temp1 != None:
            int1 += str(temp1.val)
            temp1 = temp1.next  
        
        temp2 = l2
        int2 = ''
        while temp2 != None:
            int2 += str(temp2.val)
            temp2 = temp2.next
        
        int1 = int1[: : -1]
        int2 = int2[: : -1]
        result = str(int(int1) + int(int2))

        node = ListNode(result[0])
        for i in range(1, len(result)):
            temp = node
            node = ListNode(int(result[i]))
            node.next = temp
        return node
        
