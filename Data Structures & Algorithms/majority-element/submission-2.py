from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = defaultdict(int)
        majority_count, majority_e = 0, nums[0]
        
        for n in nums:
            count[n] += 1
            if count[n] > majority_count:
                majority_count = count[n]
                majority_e = n

        return majority_e  
