from typing import List

# 面试题 08.07. 无重复字符串的排列组合
class Solution:
    def permutation(self, S: str) -> List[str]:
        res = []
        def dfs(S, path):
            if S:
                res.append(list(path))
                return
            for i in range(len(S)):
                cur = S[i]
                dfs(S[:i] + S[i + 1:], path + cur)
        dfs(S,[])
        return res

    def permutation(self, S: str) -> List[str]:
        res = []

        def dfs(k):
            if k == len(S):
                res.append(list(S))
                return
            for i in range(k, len(S)):
                
                S[i], S[k] = S[k], S[i]
                dfs(k + 1)
                S[k], S[i] = S[i], S[k]
        dfs(0)
        return res