from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def swa(nums, lo, hi):
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo],
                lo += 1
                hi -= 1

        swa(nums, 0, n - k - 1)
        swa(nums, n - k, n - 1)
        swa(nums, 0, n - 1)

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = 0   # 记录移动的元素
        for i in range(n):
            cur = i
            prev = nums[i]
            # 使用while true实现do while
            while True:
                next = (cur + k) % n
                nums[next], prev = prev, nums[next],
                cur = next
                count += 1
                if next == i:
                    break
            if count == n:
                break



