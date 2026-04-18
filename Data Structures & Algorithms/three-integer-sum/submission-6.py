class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = [1, -1, -1, 0]
        res = []
        # nums = [-1, -1, 0, 1]
        nums.sort() 
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                # you held this nums[i] and find all two pairs summing up to -nums[i] already at previous i-1 step
                continue
            
            # two pointers to find the combination summing up to -nums[i]
            l, r = i+1, n-1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l+1] == nums[l]:
                        # 下一個l我現在處理過了, 可skip
                        l += 1
                    while l<r and nums[r-1] == nums[r]:
                        # 下一個r我現在處理過了, 可skip
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            
        return res




        