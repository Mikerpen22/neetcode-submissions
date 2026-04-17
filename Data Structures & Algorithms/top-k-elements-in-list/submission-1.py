class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # from collections import Counter
        # cnt = Counter(nums)
        # return [k[0] for k in cnt.most_common(k)]
        m = defaultdict(int)
        for num in nums:
            m[num] += 1
        
        frequency = [[] for _ in range(len(nums)+1)]
        for num, freq in m.items():
            frequency[freq].append(num)
        
        res = []
        for i in range(len(frequency)-1, -1, -1):
            if k <= 0:
                return res
            if frequency[i]:
                res.extend(frequency[i])
                k -= len(frequency[i])

        return res

