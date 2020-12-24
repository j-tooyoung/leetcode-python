from typing import List

# 看左边，看右边
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)
        for i in range(1, len(ratings)):  # end值取不到，
            # print(i)
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        # print(res)
        for i in range(len(ratings) - 2, -1, -1):
            # print(i)
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)
        # print(res)
        return sum(res)