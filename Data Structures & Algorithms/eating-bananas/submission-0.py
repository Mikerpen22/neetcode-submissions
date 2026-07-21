class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # looking for a k between (1, max(piles))

        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = l + (r - l) // 2
            totalTime = 0

            for pile in piles:
                t = math.ceil(pile / mid)
                totalTime += t
            if totalTime > h:
                l = mid + 1
            elif totalTime <= h:
                res = mid
                r = mid - 1
        return res