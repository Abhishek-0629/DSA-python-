class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        n=len(prices)
        for i in range(n-1):
            sum1=prices[i]+prices[i+1]
            if money>=sum1:
                return money-sum1
        return money 

           