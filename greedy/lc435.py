from typing import List

# 435. 无重叠区间
# 寻找最多不重复区间个数cnt，length- cnt即为删除的最少个数
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        # print(intervals)
        length = len(intervals)
        cnt = 0
        end = -0x3f3f3f3f
        i = 0
        while i < length:
            while i < length and intervals[i][0] < end:
                i += 1
            print(i)
            if i < length:
                end = intervals[i][1]
                cnt += 1
        # print(cnt)
        return length - cnt