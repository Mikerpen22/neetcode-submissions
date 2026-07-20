class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        seenS1 = [0] * 26
        seenS2 = [0] * 26
        for i, c in enumerate(s1):
            seenS1[ord(c) - ord('a')] += 1
            seenS2[ord(s2[i]) - ord('a')] += 1
        

        # Sliding window of length len(s1) over s2.
        # seenS2 keeps the character counts for the current window.
        # If the counts in seenS1 and seenS2 match, then the current window
        # is a permutation of s1 (same letters, same frequencies).
        l = 0
        for r in range(len(s1), len(s2)):
            if seenS1 == seenS2: 
                return True
            
            seenS2[ord(s2[r]) - ord('a')] += 1
            seenS2[ord(s2[l]) - ord('a')] -= 1
            l += 1

        return seenS1 == seenS2
