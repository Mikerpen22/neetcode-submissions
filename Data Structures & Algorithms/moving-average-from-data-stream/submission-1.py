from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        # Create a deque to handle this, since we can push at one end, pop at the other
        self.q = deque()
        self.size = size
        self.moving_sum = 0.0

    def next(self, val: int) -> float:
        # window still has space
        if len(self.q) < self.size:
            self.moving_sum += val
            self.q.append(val)
            return self.moving_sum / len(self.q)
            
            
        else:
            # q is full, need to pop left first
            self.moving_sum -= self.q.popleft()
            self.moving_sum += val
            self.q.append(val)
            return self.moving_sum / len(self.q)

        



        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
