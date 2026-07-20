class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        seenS1 = [0] * 26
        seenS2 = [0] * 26
        for i, c in enumerate(s1):
            seenS1[ord(c) - ord('a')] += 1
            seenS2[ord(s2[i]) - ord('a')] += 1
        

        # two pointer sliding window (for seenS2)
        # if at any point the two window are identical, i.e. has same char & char cnt
        # means s1 is a permutation
        l = 0
        for r in range(len(s1), len(s2)):
            if seenS1 == seenS2: 
                return True
            
            seenS2[ord(s2[r]) - ord('a')] += 1
            seenS2[ord(s2[l]) - ord('a')] -= 1
            l += 1

        return seenS1 == seenS2
