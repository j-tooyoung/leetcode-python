from typing import List

from tree.TreeNode import TreeNode
# 后续遍历 左右中    中左右 前序遍历 调整为 中右左 ，reverse为 左右中
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        st = []
        if not root:
            return res
        st.append(root)
        while st:
            node = st.pop()
            res.append(node.val)
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        # res.reverse()
        # return res
        return list(reversed(res))  # 等价方法

