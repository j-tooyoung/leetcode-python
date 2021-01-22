from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # k = (coordinates[0][1] -coordinates[1][1]) / (coordinates[0][0] -coordinates[1][0])
        a,b=coordinates[0][0] -coordinates[1][0],coordinates[0][1] -coordinates[1][1]
        for i in range(2, len(coordinates)):
            dx, dy = coordinates[0][0] -coordinates[i][0],coordinates[0][1] -coordinates[i][1]
            if dx*b != dy*a:
                return False
        return True


