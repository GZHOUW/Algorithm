'''
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
  Input: 1->2->3->4->5->NULL, m = 2, n = 4
  Output: 1->4->3->2->5->NULL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        if not head:
            return head
        cur, prev = head, None
        for _ in range(m-1):
            prev = cur  # prev -->1
            cur = cur.next # cur --> 2
        tail = cur # tail --> 2
        con = prev # con --> 1
        for _ in range(n-m+1):
            next = cur.next # next --> 3 --> 4 --> 5 --> 6
            cur.next = prev # form circular list: 2 --> 1 --> 2 --> 1 ....
            # move prev and cur one step forward
            prev = cur # prev --> 2 --> 1 --> 2 --> 1 ...
            cur = next # cur --> 3 --> 4 --> 5 --> 6
        if con:
            con.next = prev
        else:
            head = prev
        tail.next =  next
        return head
