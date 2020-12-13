from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) == len(set(nums)):
        #     return False
        # return True
        return True if len(nums) != len(set(nums)) else False



        # s = set()
        # for i in nums:
        #     if i in s:
        #         return True
        #     s.add(i)
        # return False


