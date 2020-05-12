'''
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseIter(self, head):
        res = None
        while head != None:
            # remove the first element from head and append it to res
            temp = head # 1 2 3 4 5 None
            head = head.next # 2 3 4 5 None
            temp.next = res # temp = 1 None
            res = temp # temp = 1 None
        return res

    def reverseRecur(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        self.head = head
        self.helper(head)
        return self.head
    
    def helper(self, curr): # curr = [1,2,3,4,5,None]
        if curr.next == None:
            self.head = curr # this line is run when the last node is reached. Set it as head of reversed list
            return # return to the previous level
        
        self.helper(curr.next) # go to next level 
        
        curr.next.next = curr # this line is run when code returns to second to last level, i.e. cur = 4
        # cur is 4, cur.next is 5, cur.next.next is None.
        # Now set cur.next.next to 4, which means curr = 4 ----> 5 ------> 4
        # Note that head is also pointed at 5
        
        curr.next = None # break the link between 4(curr) and 5 
        # head = 5 ----> 4
