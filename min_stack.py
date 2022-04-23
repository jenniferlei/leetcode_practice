# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

class MinStack:
    """stack object"""
    
    def __init__(self):
        """initialize the stack object"""
        self.stack = []
        self.minStack = []
        
    def push(self, val) -> None:
        """push the element val onto the stack"""
        self.stack.append(val)

        # # if minStack is empty, append val
        # if not self.minStack or val < self.minStack[-1]:
        #     self.minStack.append(val)
        # # if val < last item of minStack, append val else append last item of minStack
        # else:
        #     self.minStack.append(self.minStack[-1])

        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
                

    def pop(self) -> None:
        """remove the element on the top of the stack"""
        
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        """get the top element of the stack"""
        return self.stack[-1]

    def get_min(self) -> int:
        """retrieve the minimum element in the stack"""
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.get_min()) # return -3
minStack.pop()
print(minStack.top()) # return 0
print(minStack.get_min()) # return -2