'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack: 
    def __init__(self):
        self.stack = []

    def push(self, x):
        if len(self.stack) == 0: # empty
            MIN = x
        else:
            MIN = min(x, self.stack[-1][1])
        self.stack.append((x, MIN))

    def pop(self):
        self.stack.pop()
        
    def top(self):
        return self.stack[-1][0] # last set, first element

    def getMin(self) -> int:
        return self.stack[-1][1] # last set, second element


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
