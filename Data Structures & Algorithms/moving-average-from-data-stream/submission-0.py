from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        # Create a deque to handle this, since we can push at one end, pop at the other
        self.q = deque(maxlen = size)
        self.m_avg = 0.0

    def next(self, val: int) -> float:
        self.q.append(val)
        return sum(self.q)/len(self.q)



        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
