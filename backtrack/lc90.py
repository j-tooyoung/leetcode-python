from typing import List

# 90. 子集 II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        nums.sort()

        def dfs(nums, start):
            res.append(list(path))  # path为引用
            st = set()
            for i in range(start, n):
                if nums[i] in st:
                    continue
                st.add(nums[i])
                path.append(nums[i])
                dfs(nums, i + 1)
                path.pop()

        dfs(nums, 0)
        return res
