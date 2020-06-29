'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root):
        self.nodeList = [] # an ascending list containing all node vals in the BST
        self.traverse(root)
        self.pointer = 0 # the current node
        
    def traverse(self, node):
        if not node:
            return
        self.traverse(node.left)
        self.nodeList.append(node.val)
        self.traverse(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        val = self.nodeList[self.pointer]
        self.pointer += 1
        return val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.pointer < len(self.nodeList)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
