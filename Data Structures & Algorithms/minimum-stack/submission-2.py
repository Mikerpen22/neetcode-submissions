from collections import deque


class MinStack:

    def __init__(self):
        self.minStk = deque() # ensure minStk[-1] is always min
        self.stk = deque()

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.minStk:
            self.minStk.append(min(val,self.minStk[-1]))
        else:
            self.minStk.append(val)
        
        

    def pop(self) -> None:
        self.stk.pop()
        self.minStk.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.minStk[-1]
        
