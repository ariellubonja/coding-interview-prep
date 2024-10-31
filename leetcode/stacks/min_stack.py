class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = 2 ** 31 # Max for this problem is 2 ^ 31 - 1
        

    def push(self, val: int) -> None:
        self.min_element = min(val, self.getMin())
        # min element at current stack situation
        self.stack.append((val, self.min_element))
        

    def pop(self) -> None:
        self.stack.pop()
        # Stack will never be empty when pop() is called, but might be after?
        if self.stack:
            self.min_element = self.stack[-1][1]
        else:
            self.min_element = 2 ** 31# What should this be when stack is empty?
            # Shouldn't matter bcs. of constraints
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.min_element
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()