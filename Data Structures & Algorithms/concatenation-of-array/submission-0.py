class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        nums.extend([i for i in nums])
        return nums