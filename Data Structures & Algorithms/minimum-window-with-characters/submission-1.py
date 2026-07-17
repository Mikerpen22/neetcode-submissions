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

        res = [-1, -1]
        resLen = float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                left_char = s[l]
                window[left_char] -= 1
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                l += 1

        l, r = res
        return "" if resLen == float("inf") else s[l:r + 1]