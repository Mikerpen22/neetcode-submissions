class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        seen = [0] * 26
        for c in s1:
            seen[ord(c) - ord('a')] += 1
        
        for l in range(len(s2)):
            r = l + len(s1) - 1
            if r >= len(s2):
                break

            curSeen = [0] * 26
            for i in range(l, r+1):
                curSeen[ord(s2[i]) - ord('a')] += 1

            if curSeen == seen:
                return True
                
        return False





