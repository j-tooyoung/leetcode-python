from typing import List


#  491. 递增子序列
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        def dfs(nums, path, start):
            if len(path) >= 2:
                res.append(list(path))
            st = set()
            for i in range(start, length):
                # 同一层for选择不能同样的元素
                if nums[i] in st:
                    continue
                if not path or path[-1] <= nums[i]:
                    # print(i)
                    st.add(nums[i])
                    path.append(nums[i])
                    dfs(nums, path, i + 1)
                    path.pop()

        dfs(nums, [], 0)
        return res

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # fixme
        res = []
        length = len(nums)
        nums.sort()
        def dfs(nums, path, start):
            if len(path) >= 2:
                res.append(list(path))
            for i in range(start, length):
                # 同一层for选择不能同样的元素
                if i >= 1 and nums[i] == nums[i-1]:
                    continue
                if not path or path[-1] <= nums[i]:
                    path.append(nums[i])
                    dfs(nums, path, i + 1)
                    path.pop()

        dfs(nums, [], 0)
        return res