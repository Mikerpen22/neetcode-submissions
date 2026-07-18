from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = deque()
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stk and stk[-1][1] < temp:
                idx, value = stk.pop()
                res[idx] = (i-idx)
            stk.append((i, temp))

        return res