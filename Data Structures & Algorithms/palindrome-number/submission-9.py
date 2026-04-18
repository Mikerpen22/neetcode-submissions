from collections import deque


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        dq = deque(s)
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True
