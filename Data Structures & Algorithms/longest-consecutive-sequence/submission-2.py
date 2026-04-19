class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        
        num_set = set(nums)
        res = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                acc = 1
                
                while curr_num + 1 in num_set:
                    curr_num += 1
                    acc += 1
                
                res = max(res, acc)

        return res