from typing import List

# 77. 组合
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(n, k, index, tmp):
            # 剪枝，剩下的数量不足时
            if n - index + 1 + len(tmp) < k:
                return
            if len(tmp) == k:
                # print(res)
                res.append(list(tmp))   # 需要新对象，否则返回为空
                return
            for i in range(index, n + 1):   # 或者修改这剪枝 for i in range(index, n- (k - len(tmp)) + 1):
                tmp.append(i)
                backtrack(n, k, i + 1, tmp)
                tmp.pop()

        backtrack(n, k, 1, [])
        # tmp = []
        # def backtrack(n, k, index):
        #     # 剪枝，剩下的数量不足时
        #     if n - index + 1 + len(tmp) < k:
        #         return
        #     if len(tmp) == k:
        #         # print(res)
        #         res.append(list(tmp))   # 需要新对象，否则返回为空
        #         return
        #     for i in range(index, n + 1):
        #         tmp.append(i)
        #         backtrack(n, k, i + 1)
        #         tmp.pop()
        # backtrack(n, k, 1)
        return res
