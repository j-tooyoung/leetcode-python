from typing import List

from tree.TreeNode import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        st = []
        res = []
        if not root: return res
        st.append(root)
        while st:
            node = st.pop()
            res.append(node.val)
            # if node.right != None: st.append(node.right)
            # if node.left != None: st.append(node.left)
            if node.right: st.append(node.right)  # 两种判断空都可以
            if node.left: st.append(node.left)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if not root: return res

        def dfs(root):
            nonlocal res
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
