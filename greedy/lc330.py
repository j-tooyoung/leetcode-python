from typing import List

# 330. 按要求补齐数组
# need to
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res = 0
        index = 1
        i = 0
        while index <= n:
            if i >= len(nums) or nums[i] > index:
                index *= 2
                res += 1
            else:
                index += nums[i]
                i += 1
        return res
