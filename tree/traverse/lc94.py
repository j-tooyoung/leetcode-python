import collections
from typing import List

from tree.TreeNode import TreeNode

# 中序遍历
# 那么再看看中序遍历，中序遍历是左中右，先访问的是二叉树顶部的节点，
# 然后一层一层向下访问，直到到达树左面的最底部，再开始处理节点（也就是在把节点的数值放进result数组中），
# 这就造成了「处理顺序和访问顺序是不一致的。」
# https://mp.weixin.qq.com/s/c_zCrGHIVlBjUH_hJtghCg
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        st = []
        if not root: return res
        while st or root:
            while root:
                st.append(root)
                root = root.left
            node = st.pop()
            res.append(node.val)
            if node.right:
                root = node.right
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        st = []
        if not root: return res
        while st or root:
            if root:                # 指针来访问节点，访问到最底层
                st.append(root)     # 讲访问的节点放进栈
                root = root.left    # 左
            else:
                node = st.pop()         # 取出数据
                res.append(node.val)  # 中
                root = node.right     # 右
        return res