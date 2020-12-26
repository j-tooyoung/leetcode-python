from typing import List

# 46. 全排列
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)

        def dfs(nums, used):
            if len(path) == n:
                res.append(list(path))
            st = set()
            for i in range(n):
                if used[i] or nums[i] in st:
                    continue
                st.add(nums[i])
                used[i] = True
                path.append(nums[i])
                dfs(nums, used)
                path.pop()
                used[i] = False

        dfs(nums, [False] * n)
        return res