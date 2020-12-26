from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        n = len(heights)
        for i in range(n):
            # 遍历每个柱子，以当前柱子的高度作为矩形的高h，
            # 从当前柱子向左右遍历，找到矩形的宽度w。
            w, h, j = 1, heights[i], i - 1
            while j >= 0 and heights[j] >= h:
                w += 1
                j -= 1
            j = i + 1
            while j < n and heights[j] >= h:
                w += 1
                j += 1
            area = max(area, w * h)
        return area

    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while st and heights[st[-1]] > heights[i]:
                j = st.pop()
                res = max(res, (i - st[-1] - 1) * heights[j])
            st.append(i)

        return res
