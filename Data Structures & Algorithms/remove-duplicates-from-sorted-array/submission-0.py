class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_k = 0
        seen = set()

        for _, n in enumerate(nums):
            if n not in seen:
                seen.add(n)
                nums[unique_k] = n
                unique_k += 1
        
        return unique_k

