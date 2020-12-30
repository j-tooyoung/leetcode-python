from heapq import heappush, heappop
from queue import PriorityQueue
from typing import List

# https://docs.python.org/3.7/library/heapq.html
# 优先队列使用，默认是小顶堆
# 大顶堆，加入负号
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # pq = PriorityQueue()
        # for i in stones:
        #     pq.put(i)
        # while pq:
        #     num1 = pq.get()
        #     num2 = pq.
        heap = []
        for i in stones:
            heappush(heap, -i)
        while len(heap) > 1:
            num1 = -heappop(heap)
            num2 = -heappop(heap)
            if num1 == num2:
                continue
            else:
                heappush(heap, -abs(num1-num2))
        if len(heap) >= 1:
            return -heappop(heap)
        else:
            return 0






