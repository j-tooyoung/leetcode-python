import collections
from queue import Queue
from typing import List

from bfs.TreeNode import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = collections.deque()
        queue.append(root)
        level = 0
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            # print(tmp)
            if level % 2 == 0:
                res.append(tmp)
                # print(res)
            else:
                print(reversed(tmp))
                res.append(tmp[::-1])
            level += 1
        return res

    def zigzagLevelOrder1(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(root, level):
            if not root: return
            if len(res) == level:
                res.append([])
            if level % 2 == 0:
                # res[-1].append(root.val)
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return res

