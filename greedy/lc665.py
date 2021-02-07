from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums = [float('-inf')] + nums + [float('inf')]
        cnt = 0
        for i in range(2, len(nums) - 1):
            # print(nums[i])
            if nums[i] < nums[i - 1]:
                if nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
                cnt += 1
        # print(cnt)
        return cnt <= 1
