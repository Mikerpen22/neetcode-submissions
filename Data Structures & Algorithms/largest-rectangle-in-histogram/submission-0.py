# 沒解出來，需注意

from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = deque() # store (start index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i

            # 如果我目前的高度比我的前一個矮 -> 前一個無法再往右擴張他的面積 -> 這就pop stack的條件
            # pop 的時候需要同時計算並更新可能最大面積
            # 一個tricky的地方是不是pop掉就沒事，因爲前面的比我高，代表我能從他那個位置延伸到我
            # so my start idx needs to be updated as well
            while stk and stk[-1][1] > h:
                index, height = stk.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            
            stk.append((start, h))
        
        # 上面for loop過完之後stack可能有殘值
        # i.e. [(1,1), (2,2), (3,3)]
        # 這裡面每個都能向右延伸到底 （不然早就被pop掉了）
        while stk:
            index, height = stk.pop()
            maxArea = max(maxArea, height * (len(heights)-index))
        
        return maxArea


        