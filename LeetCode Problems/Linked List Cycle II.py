'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list.

Example 1:
  Input: head = [3,2,0,-4], pos = 1
  Output: tail connects to node index 1
  Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
  Input: head = [1,2], pos = 0
  Output: tail connects to node index 0
  Explanation: There is a cycle in the linked list, where tail connects to the first node.
  
Example 3:
  Input: head = [1], pos = -1
  Output: no cycle
  Explanation: There is no cycle in the linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        
        # Find the node where slow and fast meet for the first time, name it pointer2
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
                
        if not fast or not fast.next:    
            return None
        
        pointer1 = head
        pointer2 = slow # or fast
        
        # increment by 1 from head (pointer1) and pointer2 at the same time, their meeting node is the res
        # a+b+c+b == 2(a+b) ---> a = c
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        return pointer1
