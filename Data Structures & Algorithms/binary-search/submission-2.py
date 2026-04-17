class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
    
        l, r = 0, len(nums)-1

        while l <= r:
            print(f"l = {l}, r = {r}")
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return -1