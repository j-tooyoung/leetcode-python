from bisect import bisect_left, bisect_right
from itertools import accumulate
from typing import List


# 5643. 将数组分成三个子数组的方案数
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        pre = list(accumulate(nums))
        ans = 0
        for i in range(n):
            l = max(i + 1, bisect_left(pre, pre[i] + pre[i]))
            r = min(n - 1, bisect_right(pre, (pre[i] + pre[-1]) // 2))
            ans = (ans + max(0, r - l) % mod)

        return ans % mod
