class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()
        d2 = dict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                return False
            if t[i] not in d2:
                d2[t[i]] = s[i]
            elif d2[t[i]] != s[i]:
                return False
        return True
