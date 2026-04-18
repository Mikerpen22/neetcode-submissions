class Solution:
    def reverse(self, x: int) -> int:
        s = ""
        isNeg = False
        if x < 0:
            isNeg = True
            s = str(-x)
        else:
            s = str(x)
        
        rev = s[::-1]
        if isNeg:
            return -int(rev) if -int(rev) >= -2**31 else 0
        else:
            return int(rev) if int(rev) <= 2**31 else 0
        

        