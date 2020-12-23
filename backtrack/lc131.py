import functools
from typing import List

# 131. 分割回文串
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        is_palindromic_string = lambda s: s == s[::-1]  # 回文串判定函数
        # @functools.lru_cache list 不能hash
        def back(s, start, tmp):
            if start == len(s):
                res.append(list(tmp))       # 引用必须拷贝一份
                return
            for i in range(start, len(s)):
                # t = s[start:i + 1]
                if s[start:i + 1] == s[start:i + 1][::-1]:
                    tmp.append(s[start:i + 1])
                    back(s, i + 1, tmp)
                    tmp.pop()
                # reversed(t)
                # if s[start: i + 1] == t:
                # if s[start: i + 1] == s[i:start-1:-1]:
                # if is_palindromic_string(s[start: i + 1]):

        back(s, 0, [])
        return res