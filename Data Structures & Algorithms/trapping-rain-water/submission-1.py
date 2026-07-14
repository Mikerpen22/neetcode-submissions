class Solution:
    def trap(self, height: List[int]) -> int:
        # the idea:
        # for any point, the contribution is `min(maxLeft, maxRight) - current`
        n = len(height)
        l, r = 0, n-1

        maxLeft, maxRight = height[l], height[r]
        # [2,1,0,1]
        # __
        #    | __       __
        #    |    | __ | 
        area = 0
        
        while l < r:
            if maxLeft < maxRight:
                # 目前左側是bottleneck
                l += 1
                maxLeft = max(maxLeft, height[l])
                area += (maxLeft - height[l])
                
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                area += (maxRight - height[r])

        return area