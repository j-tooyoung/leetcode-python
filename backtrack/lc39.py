from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tmp = []
        # sorted(candidates)    # 不排序 ？？
        candidates.sort()
        def backtrack(candidates, target, start):
            if target == 0:
                res.append(list(tmp))
                return
            for i in range(start, len(candidates)):
                if target < 0 or target < candidates[i]:
                    return
                tmp.append(candidates[i])
                backtrack(candidates, target - candidates[i], i)
                tmp.pop()
        backtrack(candidates, target, 0)
        return res
