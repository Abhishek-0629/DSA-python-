class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mini_prices=prices[0]
        max_profit=0
        for prices in prices:
            if prices<mini_prices:
                mini_prices=prices
            p=prices - mini_prices
            if p> max_profit:
                max_profit=p
        return max_profit 

       