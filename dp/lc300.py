from typing import List

# 300. 最长递增子序列
def binarySearch(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        # 二分查找，找到列表中小于i的最大元素所在的index
        mid = l + r + 1 >> 1
        if arr[mid] >= target:
            r = mid - 1
        else:
            l = mid
    return l

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        ans = 1
        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        # return max(dp)
        return ans

    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        INF = 10e9 + 10
        m =[-INF] + [INF] * length
        ans = 1
        for i in range(length):
            index = binarySearch(m, nums[i])
            print(index)
            dp[i] = index
            if index + 1 < length and m[index + 1] > nums[i]:   #  判断当前元素结尾的序列是否可以更新m
                m[index + 1] = nums[i]
            ans = max(ans, dp[i])
        return ans