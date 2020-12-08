
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        str1 =""
        for i in range(1,n+1):
            str1+= str(bin(i)[2:])
        r = int(str1,2)
        return r%(10**9+7)

