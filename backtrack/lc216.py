from typing import List

#
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        if k * 9 <= n:
            return res
        def backtrack(k, n, start, tmp):
            if len(tmp) > k or n < 0:
                return
            if len(tmp) == k and n == 0:
                res.append(list(tmp))
                return
            for i in range(start, 10):
                tmp.append(i)
                backtrack(k, n - i, i + 1, tmp)
                tmp.pop()
        backtrack(k, n, 1, [])
        return res