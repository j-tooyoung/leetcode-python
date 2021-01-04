from typing import List

# 605. 种花问题
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
            if n <= 0:
                return True

    # 计算两个1之间有多少个0，要放下n个1至少需要2n+ 1个零，prev =-1.
    # 左边界 10， prev = -2
    # 左边界 01， prev = len + 1
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = -2
        # print(len(flowerbed))
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 1:
                print(prev, i)
                n -= (i - prev - 2) // 2
                prev = i
            if n <= 0:
                return True
        # print(prev, len(flowerbed) + 1)
        n -= (len(flowerbed) - prev - 1) // 2

        return n <= 0