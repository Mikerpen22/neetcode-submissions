class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                # 最小值在mid右邊
                l = mid + 1

            else:
                # 最小值在mid左邊或是mid本身
                r = mid
        
        return nums[l]


