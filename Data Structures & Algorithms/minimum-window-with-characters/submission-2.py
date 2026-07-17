# 需要注意的題目

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        window = {}
        have = 0
        need = len(countT)

        res = [-1, -1]  # 存目前candidate (start idx, end idx)
        resLen = float("inf")

        # Two pointer:
        # 1. work on current right pointer
        # 2. adjust current window frequency set 
        # 3. if current char count is == countT[right pointer] -> have += 1
        # 4. now we update the window size if possible + update pointers
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            # 更新window size + update pointers
            while have == need:
                # 現在發現的window更短，可以更新resLen
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                left_char = s[l]
                window[left_char] -= 1
                # this left char是我們需要的，但現在被移除而且沒有存貨了-> 需要更新have
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                l += 1

        l, r = res
        return "" if resLen == float("inf") else s[l:r + 1]