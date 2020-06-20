# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None
        size = 1
        last = head
        # get the size of LL
        while last.next != None:
            last = last.next
            size += 1
        
        last.next = head  # head becomes circular list: 1 2 3 4 5 6 -->
                          #                             | <-----------| 
        k = k % size # in case k is greater thean size
        
        first = head
        for i in range(size - k - 1): # stop one element before the beginning of rotated part
            first = first.next  
        
        # first = 4 5 6 1 2 3 4....
        
        second = first.next  # second = 5 6 1 2 3 4 ..
        first.next = None  # break circular list
        
        # first = 4 None
        # second = 5 6 1 2 3 4 None
        return second
