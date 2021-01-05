from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        # for i in range(len(s)):
        i = 0
        length = len(s)
        while i < length:
            j = i
            while j < length and s[j] == s[i]:
                j += 1
            if j - i >= 3:
                res.append([i, j - 1])
            i = j
        return res