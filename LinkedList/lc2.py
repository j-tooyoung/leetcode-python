class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(-1, None)
        root = node
        v3 = 0
        while l1 != None or l2 != None:
            v1 = l1.val if (l1 != None) else 0
            v2 = l2.val if (l2 != None) else 0
            v3 += v1 + v2
            node.next = ListNode(v3 % 10, None)
            node = node.next
            v3 //= 10
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        if v3 > 0:
            node.next = ListNode(v3, None)

        return root.next
