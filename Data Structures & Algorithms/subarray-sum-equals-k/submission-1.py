class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        psum = defaultdict(int)
        psum[0] = 1
        res = 0 
        running_sum = 0

        for num in nums:
            running_sum += num
            # if (running_sum - k) in psum that means how many answer we can add
            res += psum[running_sum - k]
            # update our prefix sum
            psum[running_sum] += 1
        return res





        


