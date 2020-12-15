
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digit = list(str(N))
        n = len(digit)
        flag = n
        for i in range(n - 1, 0, -1):
            if digit[i] < digit[i - 1]:
                digit[i - 1] = str(int(digit[i - 1]) - 1)
                flag = i
        print(digit)
        digit = ''.join(digit)
        print(digit)
        return int(digit[:flag] + '9' * (len(digit) - flag))




