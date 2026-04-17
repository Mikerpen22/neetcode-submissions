class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        stk = deque()
        max_len = 0
        cur_len = 0
        for i, c in enumerate(s):
            print(f"cur stack = {stk}; cur_len = {cur_len}")
            # if element is already seen
            if len(stk) and c in stk:
                # update max length
                max_len = max(max_len, cur_len)
                # remove up to that element
                while len(stk) and stk[0] is not c:
                    stk.popleft()
                stk.popleft()
                # now append current element, reset cur_len
                stk.append(c)
                cur_len = len(stk)
            
            else:
                stk.append(c)
                cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len



        