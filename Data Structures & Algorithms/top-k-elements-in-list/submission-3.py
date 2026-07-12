from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Min-Heap to store (freq[num], num)
        # O(mlog(k)), m: # of unique elements

        # 2. Bucket Sort
        n = len(nums) # a single element's frequency is at most n
        freq_bucket = [[] for i in range(n)]
        
        # count elements
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # put into frequency bucket
        for num in count.keys():
            freq = count[num]
            freq_bucket[freq-1].append(num)

        # now simple, just traverse from the end of frequency bucket till we reach k elements
        res = []
        found = 0
        i = n-1
        while found < k and i >= 0:
            for n in freq_bucket[i]:
                if found < k:
                    res.append(n)
                    found += 1
                else:
                    break
            i -= 1
            
        return res
        
            


