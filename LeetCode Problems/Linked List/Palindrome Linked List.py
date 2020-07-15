'''
Given a singly linked list, determine if it is a palindrome.

Example 1:
    Input: 1->2
    Output: false

Example 2:
    Input: 1->2->2->1
    Output: true
    
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # now, slow is the second half
        # reverse the second half
        prev = None
        while slow :
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        # now, slow is None, and prev is the head of reversed 2nd half
        # compare the first half with the reversed 2nd half
        while prev:
            if prev.val != head.val:
                return False
            else:
                prev = prev.next
                head = head.next
        return True
            
