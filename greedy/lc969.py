from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k = len(arr)
        res = []
        while k:
            idx = arr.index(k)
            res.append(idx + 1)
            arr = arr[:idx + 1][::-1] + arr[idx + 1:]
            res.append(k)
            arr = arr[:k][::-1] + arr[k:]
            k -= 1
        print(arr)
        return res
