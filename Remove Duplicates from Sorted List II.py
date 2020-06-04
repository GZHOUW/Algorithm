'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.

Example 1:
  Input: 1->2->3->3->4->4->5
  Output: 1->2->5

Example 2:
  Input: 1->1->1->2->3
  Output: 2->3
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(head.val + 1) # different from first node so that the first node can be removed if second node = first node
        dummy.next = head

        prev = dummy
        cur = head

        
        while cur and cur.next:
            if cur.next.val != cur.val:
                prev = cur
                cur = cur.next
            else:
                while cur.next and cur.next.val == cur.val: # move cur to the last of cur's duplicate
                    cur = cur.next
                prev.next = cur.next # connect prev and cur.next, which is a different number
                cur = cur.next
        
        return dummy.next
