
class MinStack(object):
    def __init__(self):
        self.stack=[]
        self.stack_min=[float('Inf')]
        
    def push(self, x):
        self.stack.append(x)
        self.stack_min.append(min(self.stack_min[-1],x))
        
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.stack_min.pop()
            
    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.stack_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()