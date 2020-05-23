'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''

def deleteDuplicates(head):
    cur = head
    while cur: # cur becomes None at last element
        n = cur.next
        # move n to n.next until all duplicates are passed
        while n and n.val == cur.val: # n might become None
            n = n.next
        cur.next = n # set cur to n, which is next non-duplicate
        cur = cur.next
    return head
    
