class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for r, price in enumerate(prices):
            cur_profit = price - prices[l]
            
            if cur_profit < 0:
                # 買在l賣在r會賠錢
                # 那不然買在r還平盤
                l = r
            
            if cur_profit > max_profit:
                max_profit = cur_profit

            else:
                pass
        return max_profit
                


            
            



            

        