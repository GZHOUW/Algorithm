'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])

Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def middleNode(head):
    s = head
    while s != None and s.next != None: # two valid nodes
        s = s.next.next # when s goes to end head is at mid
        head = head.next

    return head
    '''
    size = 0
    s = head
    while s != None:
        s = s.next
        size += 1
    mid = size//2 

    i = 0
    while i < mid:
        head = head.next
        i += 1
    return head
    '''
