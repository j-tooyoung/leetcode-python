from LinkedList.lc2 import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: return head
        dummpy1 = ListNode(-1)
        dummpy2 = ListNode(-1)
        l1 = dummpy1
        l2 = dummpy2
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        # print(l3.next)
        #
        l2.next = None
        l1.next = dummpy2.next
        return dummpy1.next