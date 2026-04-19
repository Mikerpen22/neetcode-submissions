class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                count = 1
                candidate = num
                continue
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate