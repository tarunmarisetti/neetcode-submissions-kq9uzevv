class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        buy_price=prices[0]
        for price in prices[1:]:
            profit=price-buy_price
            max_profit=max(max_profit,profit)
            buy_price=min(buy_price,price)
        return max_profit
            
        