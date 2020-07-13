'''
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    if not head:
        return None
    # EX: 1 2 3 4 5 6
    odd = head
    even = head.next
    evenHead = even
    while even != None and even.next != None:

        odd.next = odd.next.next # odd = 1 3 4 5 6
        even.next = even.next.next # even = 2 4 5 6

        # head = 1 3 4 5 6
        odd = odd.next  # odd = 3 4 5 6
        even = even.next # even = 4 5 6
        ''' 
        After loop, head = 1 3 5 6
                    odd = 5
                    even = 6
                    eHead = 2 4 6
        ''' 

    # the odd pointer currently points at the last node of the odd-node list
    odd.next = evenHead  # odd = 5 2 4 6, head = 1 3 5 2 4 6

    return head
    
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
a.next.next.next.next.next = ListNode(6)
oddEvenList(a)
