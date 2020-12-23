from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i
        return -1

    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        for i, ch  in enumerate(s):
            if d[ch] == 1:
                return i
        return -1
