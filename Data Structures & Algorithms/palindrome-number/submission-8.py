from collections import deque
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        s = str(x)
        q = deque()
        isOdd = True
        if len(s) % 2 == 1:
            mid_pos = len(s) // 2
        else:
            mid_pos = len(s) // 2 - 1
            isOdd = False
        print(f"mid_pos = {mid_pos}")
        cur = 0
        while cur <= mid_pos:
            q.append(s[cur])
            cur+=1


        if isOdd:
            q.pop()
        
        print()
        while len(q) > 0 and cur < len(s):
            
            if q.pop() == s[cur]:
                cur += 1
            else:
                return False
        return True





            


        