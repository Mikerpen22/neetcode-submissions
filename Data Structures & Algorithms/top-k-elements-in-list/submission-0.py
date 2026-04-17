class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        cnt = Counter(nums)
        return [k[0] for k in cnt.most_common(k)]