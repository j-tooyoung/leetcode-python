from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cntOf5, cntOf10 = 0, 0
        for i in bills:
            if i == 5:
                cntOf5 +=1
            elif i == 10:
                cntOf5 -=1
                cntOf10 += 1
            elif cntOf10 > 0:
                cntOf10 -= 1
                cntOf5 -= 1
            else:
                cntOf5 -= 3
            # print(cntOf5, cntOf10)

            if cntOf5 < 0:
                return False
        return True




