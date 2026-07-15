class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # two pointer -> what's the condition to move our pointer?
        # 1. as long as this condition hold true we move right pointer:
        # window length - cur max frequency char <= k (還在可替換的範圍)
        # 2. if condition breaks:
        # move left pointer till condition become true again

        l = 0
        charMap = [0] * 26
        res = 0
        
        for r in range(len(s)):
            
            charMap[ord(s[r]) - ord('A')] += 1
            windowLength = r - l + 1

            if windowLength - max(charMap) <= k:
                res = max(res, windowLength)
            else:
                while l < r and (windowLength - max(charMap) > k):
                    windowLength -= 1
                    charMap[ord(s[l]) - ord('A')] -= 1
                    l += 1
        return res



                    





