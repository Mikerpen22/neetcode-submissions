import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Python heapq 預設是 min-heap，
        # 因此存入負數，把它當成 max-heap 使用。
        max_heap = []
        res = []

        # 初始化第一個 window
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))

        # 第一個 window 的最大值
        res.append(-max_heap[0][0])

        # 從第二個 window 開始滑動
        for r in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))

            # 當前 window 左邊界
            left = r - k + 1

            # 移除已經離開 window左界 的元素
            # 我唯一需要確保的是之後讀取maxheap頂端的element一定在我的window
            while max_heap[0][1] < left:
                heapq.heappop(max_heap)

            res.append(-max_heap[0][0])

        return res