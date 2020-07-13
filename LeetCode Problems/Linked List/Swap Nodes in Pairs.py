'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if head == None:
        return None
    s = ListNode(0)
    s.next = head
    n1 = s.next # first node of current pair
    n2 = s.next.next # second node of current pair
    prev = s # the previous node of the current pair 
    
    #    p   n1   n2  next 
    #    0   1    2    3    4    5 
    
    while n2 != None: 
        nextPair = n2.next # the start of next pair nextPair = 3 4 5

        # swap n1 and n2
        prev.next = n2  # prev = 0 2 3 4 5
        n2.next = n1  # n2 = 2 1 2 3 4 5
        n1.next = nextPair  # n1 = 1 3 4 5 --> n2 = 2 1 3 4 5 (swapped)

        # n1 and n2 are now swapped
        prev = n1 # n1 is now after n2, set it as prev

        n1 = nextPair
        if nextPair == None:
            break
        n2 = nextPair.next
    return s.next
