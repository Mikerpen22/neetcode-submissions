from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []  # stores (-value, index)

        l = 0
        for r in range(len(nums)):
            heapq.heappush(heap, (-nums[r], r))

            # Remove elements that are outside the window
            while heap[0][1] < l:
                heapq.heappop(heap)

            # Once we have a full window, record the max
            if r - l + 1 == k:
                res.append(-heap[0][0])
                l += 1

        return res