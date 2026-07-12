class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we care about "frequency" of the char in each str
        # essentially, frequency is the "hash signature" of the string
        # freq -> bucket sort!

        from collections import defaultdict
        mp = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            mp[tuple(freq)].append(s)

        return list(mp.values())

