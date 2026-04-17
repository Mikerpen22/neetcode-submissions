from collections import Counter, defaultdict
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bkt = defaultdict(list)
        for s in strs:
            cnt = Counter(s)
            fs = frozenset(cnt.items())
            bkt[fs].append(s)


        return [i for i in bkt.values()]


