# import functools
from functools import lru_cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0] * 2 for i in range(len(prices))]
        print(dp)
        # 0为未持有， 1为持有状态
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][1] + prices[i] - fee, dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        return dp[len(prices) - 1][0]

    # 递归
    def maxProfit1(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)

        # 缓存
        # @functools.lru_cache
        @lru_cache(None)
        def dfs(index: int, status: int):
            if index == n:
                return 0
            a = dfs(index + 1, status)
            b, c = 0, 0
            if status:
                # 处理卖的情况
                b = dfs(index + 1, 0) + prices[index] - fee
            else:
                c = dfs(index + 1, 1) - prices[index]
            return max(a, b, c)

        return dfs(0, 0)

    # 递归
    def maxProfit2(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        d = dict()

        # 缓存
        def dfs(index: int, status: int):
            if (index, status) in d:
                return d[index,status]
            if index == n:
                return 0
            a = dfs(index + 1, status)
            b, c = 0, 0
            if status:
                # 处理卖的情况
                b = dfs(index + 1, 0) + prices[index] - fee
            else:
                c = dfs(index + 1, 1) - prices[index]
            d[index, status] = max(a, b, c)
            return max(a, b, c)
        return dfs(0, 0)