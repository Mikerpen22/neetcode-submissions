import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. 確定搜尋範圍（吃香蕉的速度 k）：
        # 最慢速度 = 1（每小時至少吃 1 根）
        # 最快速度 = max(piles)（一小時直接吃完最大那堆，再快也沒意義，因為一小時只能吃一堆）
        l, r = 1, max(piles)
        res = r  # 預設答案為最大可能速度

        # 2. 二分搜尋找出「符合條件的最小速度」
        while l <= r:
            mid = l + (r - l) // 2  # 當前測試的速度 k
            totalTime = 0

            # 3. 計算以速度 mid 吃完所有香蕉需要幾小時
            for pile in piles:
                # 無條件進位：例如 7 根香蕉以速度 3 吃，需要 ceil(7/3) = 3 小時
                t = math.ceil(pile / mid)
                totalTime += t
            
            # 4. 根據總耗時調整搜尋區間
            if totalTime > h:
                # 總時間超過限制 -> 吃的太慢了！速度必須加快
                l = mid + 1
            else:  # totalTime <= h
                # 可以在警衛回來前吃完！
                # 紀錄當前可行速度，並嘗試尋找是否有「更慢（更小）」的可行速度
                res = mid
                r = mid - 1

        return res