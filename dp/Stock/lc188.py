import functools
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        if k > n // 2:
            dp0, dp1 = 0, -prices[0],
            for i in range(n):
                tmp = dp1
                dp1 = max(dp1, dp0 - prices[i])
                dp0 = max(dp0, tmp + prices[i])
            return max(dp0, dp1)
        d = dict()
        # @functools.lru_cache
        def dfs(k, start, state):
            if (k,start, state) in d:
                return d[k,start, state]
            if start >= n or k == 0:
                return 0
            # 报错
            # return max(dfs(k, start + 1, state), dfs(k - 1, start + 1, False) + prices[start],dfs(k, start + 1, True) - prices[start])
            a, b, c = 0, 0, 0
            if state:
                a = dfs(k - 1, start + 1, False) + prices[start]
            else:
                b = dfs(k, start + 1, True) - prices[start]
            c = dfs(k, start + 1, state)
            d[k,start, state] = max(a, b, c)
            return d[k,start, state]

        return dfs(k, 0, False)
        # error
        # res = 0
        # # True 为持有， False 不持有
        # # 0买入 1卖出 2不动
        # # @functools.lru_cache list无法哈希
        # def dfs(prices, k, start, state):
        #     nonlocal res
        #     if k == 0:
        #         return res
        #     for i in range(start,len(prices)):
        #         if state:
        #             res = max(res, dfs(prices, k - 1, i + 1, False) + prices[i])
        #         else:
        #             res = max(res, dfs(prices, k, i + 1, True) - prices[i])
        #         res = max(res, dfs(prices, k, i + 1, state))
        #     return res
        #
        # return dfs(prices, k, 0, False)

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        if k > n // 2:
            dp0, dp1 = 0, -prices[0],
            for i in range(1, n):
                tmp = dp1
                dp1 = max(dp1, dp0 - prices[i])
                dp0 = max(dp0, tmp + prices[i])
            return max(dp0, dp1)
        # 设定为1000，速度最快
        # * maxsize代表缓存的内存占用值，超过这个值之后，就的结果就会被释放，然后将新的计算结果进行缓存,其值应当设为2的幂 *
        # def lru_cache(maxsize=128, typed=False): 默认128
        @functools.lru_cache(maxsize=1000)
        def dfs(k, start, state):
            if start >= n or k == 0:
                return 0
            a, b, c = 0, 0, 0
            if state:
                a = dfs(k - 1, start + 1, False) + prices[start]
            else:
                b = dfs(k, start + 1, True) - prices[start]
            c = dfs(k, start + 1, state)
            return max(a, b, c)

        return dfs(k, 0, False)