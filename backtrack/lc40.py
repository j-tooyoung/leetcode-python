from typing import List

# 40. 组合总和 II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        n = len(candidates)
        def dfs(candidates, start,target):
            if start > n or target < 0:
                return
            if target == 0:
                res.append(list(path))
            st = set()
            for i in range(start, n):
                if candidates[i] in st: continue
                st.add(candidates[i])
                path.append(candidates[i])
                dfs(candidates, i + 1, target - candidates[i])
                path.pop()

        dfs(candidates, 0, target)
        return res
