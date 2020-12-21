from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        stack =[]
        existed = set()
        for a in s:
            print(stack)
            if a not in existed:
                while stack and stack[-1] > a and c[stack[-1]] > 0:
                    existed.remove(stack.pop())
                stack.append(a)
                existed.add(a)
            c[a] -= 1
        return "".join(stack)
        # todo fixme error
        st = list()
        s1 = set()
        c = Counter(s)

        for i in range(len(s)):
            if s[i] not in s1:
                while len(st) != 0 and st[-1] > s[i] and c[st[-1]] > 0:
                    # print(st[-1], i)
                    s1.remove(st.pop())
                s1.add(s[i])
                st.append(s[i])
            c[s[i]] -= 1
        return "".join(st)
