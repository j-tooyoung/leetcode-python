class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for c1, c2 in zip(s, t):
            if hashmap1.get(c1, c2) != c2 or hashmap2.get(c2, c1) != c1:
                return False
            hashmap1[c1] = c2
            hashmap2[c2] = c1
        return True

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
