'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
  Input:
  [
    1->4->5,
    1->3->4,
    2->6
  ]
  Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        merged = ListNode(0) # always points at the first node
        p = merged # recure itself
        
        # stop loop when ONE list is finished
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next # move to next l1 value
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next
        
        # At this point, either l1.val or l2.val is None
        if l1 != None:
            p.next = l1 # no need to create new node because the rest of l1 is correctly sorted 
                        # no need for l1 = l1.next for the same reason, simply copy over
        else:
            p.next = l2

            
        return merged.next # get rid of the first "0"
