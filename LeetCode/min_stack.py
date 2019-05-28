
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stk = [] # idxes of min vals 
        self.stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        
        if len(self.min_stk) > 0:
            min_idx = self.min_stk[-1]
            if x <= self.stk[min_idx]:
                self.min_stk.append(len(self.stk)-1) # last idx
        else:
            self.min_stk.append(0) # first one
            
        
    def pop(self) -> None:
        idx_val = len(self.stk)-1
        val = self.stk.pop()
        if idx_val == self.min_stk[-1]:
            self.min_stk.pop()
            
    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        if self.min_stk:
            return self.stk[self.min_stk[-1]]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()