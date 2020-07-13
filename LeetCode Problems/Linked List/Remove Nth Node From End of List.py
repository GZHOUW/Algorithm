'''
Given a linked list, remove the n-th node from the end of list and return the entire List.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

'''

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def removeNthFromEnd(List, n):
    size = 0
    s = List
    sList = []
    while s != None: # one pass!
        sList.append(s)
        s = s.next
        size += 1
    if n == size:
        return List.next # if size <= 2, sList[size - n - 1] doesnt exist
    else:
        # let [n-1 to last item].next become [n to last item].next
        # hence the n to last item is gone, for nothing points to it anymore
        sList[size - n - 1].next = sList[size - n].next 
        return List
