class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_buy = prices[0]
        profit = 0

        # Looping through each price in the prices array
        for price in prices:
            # If the current price is less than the min_buy price so far, we update our
            # buy price
            if price < min_buy:
                min_buy = price
            else:
                # Calculate profit if we sold at the current price 
                profit = max(profit, price - min_buy)
            
        return profit
            
                
                
                
                