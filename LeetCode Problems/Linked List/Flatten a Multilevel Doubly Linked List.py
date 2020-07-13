'''
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. 
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.
Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []
 
How multilevel linked list is represented in test case:
We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 
Constraints:

Number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    
    def flattenStack(self, head):
        if not head:
            return None
        stack = [head]
        prev = Node(0) # dummy node, put before head
        while stack: 
            cur = stack.pop()
            
            # connect cur and prev, if no child, this changes nothing
            cur.prev = prev 
            prev.next = cur
            
            prev = cur # move pre to cur
            
            if cur.next:
                stack.append(cur.next) # stack will store the next node of cur level while dealing whith child nodes
            if cur.child:
                stack.append(cur.child) # put child after next node so that child will be inserted after cur
                cur.child = None
                
        head.prev = None
        return head
    
    def flattenRec(self, head):
        if not head:
            return (None)
        self.travel(head)
        return head

    def travel(self, cur):
        while cur:
            # store next node in case cur.next later points to child node. will use this to connect the child level back to current level
            next = cur.next 
            
            if not next: 
                tail = cur  # cur is last node in current level, assign it to 'tail' for return

            if cur.child: # handle the child node's level and any more child nodes that it spawns
                # connect cur and its child node
                cur.child.prev = cur
                cur.next = cur.child
                child_tail = self.travel(cur.child) # returns tail after traversing the child node's level
                
                if next:  # if there exists a node in the prior level, connect its prev pointer to the child node's tail
                    next.prev = child_tail

                child_tail.next = next  # connect child_tail back to prior level's next node
                cur.child = None  # clear child pointers
            
            cur = cur.next

        return tail  # return the tail node of cur level  
