class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = min(h_b, h_a) * (h_b - h_a)
        # find max area
        max_A = -1 # set default
        l, r = 0, len(heights)-1

        while l < r:
            A = min(heights[r], heights[l]) * (r-l)
            if A > max_A:
                max_A = A
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1

        return max_A
