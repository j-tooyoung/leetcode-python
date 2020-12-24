from typing import List

from tree.TreeNode import TreeNode

# 标记法
# 「无法同时解决访问节点（遍历节点）和处理节点（将元素放进结果集）不一致的情况」。
# 「那我们就将访问的节点放入栈中，把要处理的节点也放入栈中但是要做标记。」
# 「就是要处理的节点放入栈之后，紧接着放入一个空指针作为标记。」 这种方法也可以叫做标记法。
# https://mp.weixin.qq.com/s/WKg0Ty1_3SZkztpHubZPRg
class solution:

    def preorderTraverse(self,root: TreeNode) -> List[int]:
        return


    def inorderTraverse(self,root: TreeNode) -> List[int]:
        # res = []
        # st = []
        # if not root:
        #     st.append(root)
        # while st:
        #     node = st.pop()
        #     if node:
        #         st.pop()
        #         if node.right:
        #             st.append(node.right)
        #         st.append(node)
        #         st.append(None)
        #         if node.left:
        #             st.append(node.left)
        #     else:
        #         st.pop()
        #         node = st.pop()
        #         res.append(node.val)
        # return res
        return

    def postorderTraverse(self,root: TreeNode) -> List[int]:
        return