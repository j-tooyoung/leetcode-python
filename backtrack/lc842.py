from typing import List

#
class Solution:
    def splitIntoFinbonacci(self, S: str) -> List[int]:
        ans = list()

        def backtrack(index: int):
            if index == len(S):
                return len(ans) >= 3
            cur = 0
            for i in range(index, len(S)):
                if i > index and S[index] == '0':
                    break
                cur = cur * 10 + ord(S[i]) - ord("0")
                if cur > 2 ** 31 - 1:
                    break

                if len(ans) < 2 or cur == ans[-2] + ans[-1]  :
                    ans.append(cur)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                elif len(ans) > 2 and ans[-2] + ans[-1] < cur:
                    break
            return False

        backtrack(0)
        return ans
