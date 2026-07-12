class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ns = set(nums)
        max_len = 0

        for num in nums:
            # i need to know if current num is the "start" of the sequence
            # if my left hand side is in set that means i'm not the start
            # otherwise i'm the start
            if (num - 1) not in ns:

                # now i'm the start of the sequence, start accumulating
                next_num = num + 1
                cur_len = 1
                while next_num in ns:
                    next_num += 1
                    cur_len += 1
                    
                max_len = max(max_len, cur_len)
                
            else:
                pass
                # I'm not the "start" of the sequence
                # means i've already been dealt with
        
        return max_len





