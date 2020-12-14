from ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        tmp = head.next
        newHead = self.reverseList(head.next)
        tmp.next = head
        head.next = None
        return newHead