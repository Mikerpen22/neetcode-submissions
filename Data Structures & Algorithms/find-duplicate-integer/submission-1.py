class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # binary search in [1,n]
        # 條件是mid左右兩邊的數字，出現在nums的次數理論上會相等 (assume only appear once)
        # 如果有一邊比較大，比如左邊，代表左邊有人重複
        left, right = 1, len(nums) - 1  
        while left < right:
            mid = (left + right) // 2
            count = sum(1 for num in nums if num <= mid)
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left