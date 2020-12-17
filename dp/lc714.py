from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0]* 2 for i in range(len(prices))]
        print(dp)
        # 0为未持有， 1为持有状态
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][1] + prices[i] - fee, dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
        return dp[len(prices) - 1][0]