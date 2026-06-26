class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                total = prices[r] - prices[l]
                maxP = max(maxP, total)
            else: 
                l = r
            r += 1
        
        return maxP
