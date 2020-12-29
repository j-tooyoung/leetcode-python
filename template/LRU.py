class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        self.ok = True

class LRUCache:

    def __init__(self, capacity: int):
        self.record = {}
        self.size = 0
        self.capacity = capacity
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head


    def _add_head(self, node: ListNode) -> None:
        # 将一个节点插入到头结点之后的位置
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def _delete_node(self, node:ListNode) -> None:
        node.prev.next = node.next
        node.prev.next.prev = node.prev

    def get(self, key:int) ->int:
        # 获取一个元素
        item = self.record.get(key, None)
        if item and item.ok:
            self._delete_node(item)
            self._add_head(item)
            return item.value
        else:
            return -1

    def put(self, key:int, value:int) -> None:
        # 新增数据
        item = self.record.get(key, None)
        if item:
            item.value = value
            self.get(key)
        else:
            tmp = ListNode(key, value)
            self.record[key] = tmp
            if self.size == self.capacity:
                tmp1 = self.tail.prev
                del self.record[tmp1.key]
                self._delete_node(tmp1.key)
                self._add_head(tmp)
            else:
                self._add_head(tmp)
                self.size += 1


