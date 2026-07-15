class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque

        stk = deque()
        elementInStk = set()
        res = 1 if len(s) else 0

        # put into stk as long as there's no duplicate
        # if there's, we pop the stk up to that element
        # then continue
        for i,c in enumerate(s):
            if c not in elementInStk:
                elementInStk.add(c)
                stk.append(c)
                res = max(res, len(stk))
                continue
            else:
                while stk and stk[0] != c:
                    elementInStk.remove(stk.popleft())
                if stk:
                    stk.append(stk.popleft())
                res = max(res, len(stk))
                    
        return res
                








        