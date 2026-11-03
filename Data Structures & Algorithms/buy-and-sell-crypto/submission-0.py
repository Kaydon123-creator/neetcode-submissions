class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = ans = 0 

        for i in range(len(prices)-1):
            ans += (prices[i+1]-prices[i])
            if ans < 0:
                ans = 0 

            res = max(ans, res)
        return res
        
        