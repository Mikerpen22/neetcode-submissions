class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        profMax = 0
        entry = 0
        
        for i, price in enumerate(prices):
            if price < prices[entry]:
                # if you see a better entry, buy here instead
                entry = i
                # reset profit
                prof = 0
            else:
                # price continues to go up, keep holding
                prof = (price - prices[entry])
                profMax = max(profMax, prof)
        return profMax



