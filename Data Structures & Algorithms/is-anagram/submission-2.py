class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        used = {}
        for c in s:
            if c not in used:
                used[c] = 1
                continue
            used[c]+=1

        for c in t:
            if c in used and used[c] >= 1:
                used[c] -= 1
                if used[c] == 0:
                    used.pop(c)
            else:
                return False
        return len(used) == 0
            

            
            