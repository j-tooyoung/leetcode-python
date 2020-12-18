from collections import Counter
from functools import reduce
from operator import xor


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 计数，求和，位运算
        # return list(Counter(t) - Counter(s))[0]
        return chr(reduce(xor,map(ord, s + t)))
        return chr(sum(map(ord,t) - sum(map(ord,s))))
        # d1 = [0 for _ in range(26)]
        #
        # for i in s:
        #     d1[ord(i)-ord('a')] += 1
        # for i in t:
        #     d1[ord(i)-ord('a')] -= 1
        # for i in range(len(d1)):
        #     if d1[i] < 0:
        #         return chr(i + ord('a'))
        d1 ={}
        d2 ={}
        for i in s:
            d1[i] = d1.get(i,0) + 1
        for i in t:
            d2[i] = d2.get(i,0) + 1
        for i in d2:
            if d2[i] > d1.get(i,0):
                return i