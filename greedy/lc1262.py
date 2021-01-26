from typing import List

# 动态规划
# 贪心
# 状态机
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        a = [x for x in nums if x % 3 == 0]
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)

        ans = 0
        lb,lc = len(b),len(c),
        for j in [lb,lb-1,lb-2]:
            if j>=0:
                for k in [lc,lc-1,lc-2]:
                    if k >=0 and j%3==k%3:
                        ans = max(ans, sum(b[:j]) + sum[c[:k]])
        return ans + sum(a)
