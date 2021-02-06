from bisect import bisect_left
from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        def LIS(A):
            d = []
            for a in A:
                idx = bisect_left(d, a)
                if d and idx < len(d):
                    d[idx] = a
                else:
                    d.append(a)
            return len(d)

        B = []
        target = {t: i for i, t in enumerate(target)}
        for a in arr:
            if a in target:
                B.append(target[a])
        return len(target) - LIS(B)
