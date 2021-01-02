import collections
from collections import deque
from typing import List

# 239. 滑动窗口最大值
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        res = [0] * (len(nums)-k+1)
        for i in range(len(nums)):
            #保证从大到小 如果前面数小则需要依次弹出，直至满足要求
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            #判断队首值是否有效
            if queue[0] <= i - k:
                queue.popleft()
            #当窗口长度为k时 保存当前窗口中最大值
            if i + 1 >= k:
                res[i+1-k] = nums[queue[0]]
        return res