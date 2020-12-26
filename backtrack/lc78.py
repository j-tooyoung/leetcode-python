from typing import List


# 78. 子集
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)

        def dfs(nums, start):
            res.append(list(path))  # path为引用
            for i in range(start, n):
                path.append(nums[i])
                dfs(nums, i + 1)
                path.pop()

        dfs(nums, 0)
        return res
