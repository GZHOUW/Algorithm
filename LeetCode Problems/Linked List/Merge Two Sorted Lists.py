'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution: 
    def mergeTwoLists(self, l1, l2):
        merged = ListNode(0) # always points at the first node
        p = merged # pointer
        
        while l1 and l2: # stop loop when a list is finished
            if l1.val <= l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next # move to next l1 value
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next
        
        # At this point, either l1.val or l2.val is None
        if l1 != None:
            p.next = l1 # the rest of l1 is correctly sorted, simply copy over
        else:
            p.next = l2
        return merged.next # get rid of the first "0"
    
    # recursive solution
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2 # l1 is done, append the rest of l2 to end
        if not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            
