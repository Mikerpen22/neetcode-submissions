class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            lc, rc = s[l], s[r]
            if not lc.isalnum():
                l+=1
                continue
            if not rc.isalnum():
                r-=1
                continue
            
            if lc.lower() != rc.lower():
                return False
            l += 1
            r -= 1
        return True    
            



