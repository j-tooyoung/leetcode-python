import collections
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(length):
                if isConnected[i][j] == 1 and j not in visited:

                    visited.add(j)
                    dfs(j)

        length = len(isConnected)
        visited = set()
        cicrles = 0
        for i in range(length):
            if i not in visited:
                dfs(i)
                cicrles += 1

        return cicrles

    # bfs
    def findCircleNum1(self, isConnected: List[List[int]]) -> int:

        length = len(isConnected)
        visited = set()
        circles = 0

        for i in range(length):
            if i not in visited:
                q = collections.deque([i])
                while q:
                    j = q.popleft()
                    visited.add(j)
                    for k in range(length):
                        if isConnected[j][k] == 1 and k not in visited:
                            q.append(k)
                circles += 1

        return circles

        # union find
        def findCircleNum2(self, isConnected: List[List[int]]) -> int:

            def find(index: int) -> int:
                if parent[index] != index:
                    parent[index] = find(parent[index])
                return parent[index]

            def union(index1: int, index2: int):
                parent[find(index1)] = find(index2)

            length = len(isConnected)
            parent = list(range(length))


            for i in range(length):
                for j in range(i+1, length):
                    if isConnected[i][j] == 1:
                        union(i,j)

            circles = sum(parent[i] == i for i in range(length))
            return circles
