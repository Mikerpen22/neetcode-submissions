class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # utilize the concept of two sum variant (sorted)
        # i.e. two pointers to find the target
        nums.sort() # O(nlog(n))
        n = len(nums)
        res = []

        for i, num in enumerate(nums):
            # find the start number, but we need to skip duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # now we ahve the start number, the problem becomes:
            # [...<start>...] in subarray after start number, find two sum equals (0 - <start>)

            l, r = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    # too large, lower right bound
                    r -= 1
                elif total < 0:
                    # too small, increase left bound
                    l += 1
                else:
                    # bingo, append to res
                    # [-1, -1, 0, 0, 1, 1]
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # update to next 
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res
