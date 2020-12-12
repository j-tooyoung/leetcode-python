from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if nums == None or len(nums) < 1:
            return 0
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(down, up)

# todo FIXME ERROR
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if nums is None or len(nums) < 1:
            return 0
        dp = [[0] * 2] * len(nums)
        dp[0][0] = 1
        dp[0][1] = 0
        # 0为下降态，1为上升态
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] > nums[i]:
                    dp[i][0] = max(dp[j][1] + 1, dp[i][0])
                elif nums[j] < nums[i]:
                    dp[i][1] = max(dp[j][0] + 1, dp[i][1])
                else:
                    dp[i][1] = dp[i - 1][1]
                    dp[i][0] = dp[i - 1][0]
        return max(dp[len(nums) - 1][0], dp[len(nums) - 1][1])
