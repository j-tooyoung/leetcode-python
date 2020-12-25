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
        n = len(nums)
        # 特殊判断，如果元素数量等于组数
        if n == k:
            return 0

        value = dict()
        for sub in range(1 << n):
            # 判断 sub 是否有 n/k 个 1
            if bin(sub).count("1") == n // k:
                # 使用哈希表进行计数
                freq = set()
                flag = True
                for j in range(n):
                    if sub & (1 << j):
                        # 任意一个数不能出现超过 1 次
                        if nums[j] in freq:
                            flag = False
                            break
                        freq.add(nums[j])

                # 如果满足要求，那么计算 sub 的不兼容性
                if flag:
                    value[sub] = max(freq) - min(freq)

        f = dict()
        f[0] = 0
        for mask in range(1 << n):
            # 判断 mask 是否有 n/k 倍数个 1
            if bin(mask).count("1") % (n // k) == 0:
                # 枚举子集
                sub = mask
                while sub > 0:
                    if sub in value and mask ^ sub in f:
                        if mask not in f:
                            f[mask] = f[mask ^ sub] + value[sub]
                        else:
                            f[mask] = min(f[mask], f[mask ^ sub] + value[sub])
                    sub = (sub - 1) & mask

        return -1 if (1 << n) - 1 not in f else f[(1 << n) - 1]
