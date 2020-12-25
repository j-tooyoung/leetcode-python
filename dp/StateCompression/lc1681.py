import functools
import math
from itertools import combinations
from typing import List

# 1681. 最小不兼容性
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        # 超时
        size = len(nums) // k
        if size == 1:
            return 0
        nums.sort()
        @functools.lru_cache
        def dp(mask):
            available = [i for i in range(len(nums)) if not mask & (1 << i) ]
            if not available:
                return 0
            res = math.inf
            for arr in combinations(available[1:], size - 1):
                arr = (available[0],) + arr
                if any(nums[a] == nums[b] for a, b in zip(arr, arr[1:])):
                    continue
                mask2 = mask
                for v in arr:
                    mask2 |= 1<< v
                res = min(res, dp(mask2) + nums[arr[-1]] - nums[arr[0]])
            return res
        res = dp(0)
        return res if res != math.inf else -1

    def minimumIncompatibility(self, nums: List[int], k: int) -> int:

        return 0

