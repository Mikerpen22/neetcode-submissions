class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers
        maxA = 0
        i, j = 0, len(heights)-1

        while i < j:
            area = (j-i) * min(heights[i], heights[j])
            maxA = max(maxA, area)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return maxA
