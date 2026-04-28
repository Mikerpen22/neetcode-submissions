class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        # start from mid point to expand
        # if final answer's length is odd, setting l, r = mid will work
        # but if the answer's length is even, you'll only get 1+2n which will never work
        for mid in range(n):
            l, r = mid, mid
            while l>=0 and r<n and s[l] == s[r]:
                # ensure within string boundary and can expand!
                candidate = s[l:r+1]
                if len(candidate) > len(res):
                    res = candidate
                l -= 1
                r += 1
            l, r = mid, mid+1
            while l>=0 and r<n and s[l] == s[r]:
                # ensure within string boundary and can expand!
                candidate = s[l:r+1]
                if len(candidate) > len(res):
                    res = candidate
                l -= 1
                r += 1
        return res



            