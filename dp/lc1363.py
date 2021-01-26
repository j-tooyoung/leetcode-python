from typing import List


# 动态规划，状态机
# 贪心
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # sorted(digits)
        # digits.sort()
        digits = sorted(digits, reverse=True)
        # print(digits)
        a = [x for x in digits if x % 3 == 0]
        b = sorted([x for x in digits if x % 3 == 1], reverse=True)
        c = sorted([x for x in digits if x % 3 == 2], reverse=True)
        total = sum(digits)
        s = []
        if total == 0:
            return "0"
        if total % 3 == 0:
            return "".join(str(digits)).replace(',', '').replace(' ', '').strip('[').strip(']')
        elif total % 3 == 1:
            # 注意等号
            if len(c) < 2 or len(b) > 0 and b[-1] <= c[-1] + c[-2]:
                s = a + b[:-1] + c
            else:
                s = a + b + c[:-2]
        elif total % 3 == 2:
            if len(b) < 2 or len(c) > 0 and c[-1] <= b[-1] + b[-2]:
                s = a + b + c[:-1]
            else:
                s = a + b[:-2] + c
        s = sorted(s, reverse=True)
        # print(s)
        return "".join(str(s)).replace(',', '').replace(' ', '').strip('[').strip(']')