from bfs.TreeNode import TreeNode

# 颜色标记遍历 https://leetcode-cn.com/problems/convert-bst-to-greater-tree/solution/yan-se-biao-ji-fa-bian-li-shu-bian-li-shu-wo-tui-j/
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        stack = [(1,root)]
        res =[]
        sum =0
        while stack:
            color, curNode = stack.pop()
            if not curNode: continue
            if color ==1:
                stack.append((1,curNode.left))
                stack.append((0,curNode))
                stack.append((1,curNode.right))
            else:
                sum += curNode.val
                curNode.val = sum
        return root

