
# https://wangdh15.github.io/2020/03/24/%E6%A0%91%E7%8A%B6%E6%95%B0%E7%BB%84/#more
# 树状数组
# 每个元素不再维护其前面所有的元素的和，只维护其前面部分元素的和。下面是一个比较形象的说明：
# 树状数组的实现
# 每个节点的父节点是：x + lowbit(x)
# 每个节点的直接孩子节点是 x - lowbit(x)
# lowbit(x) = x & -x

class SegemtTree:

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)


    def _lowbit(self, index):
        return index & (-index)

    def update(self,index, delta):
        while index < self.size:
            self.tree[index] += delta
            index += self._lowbit(index)

    def query(self, index ):
        res = 0
        # 注意：树状数组的下标是从1开始而不是零，否则会死循环
        while index >= 1:
            res += self.tree[index]
            index -= self._lowbit(index)
        return res

    def query_inter(self, l, r):
        return self.query(r) - self.query(l-1)

    @classmethod
    def built_from_list(cls, _list):
        length = len(_list)
        tmp = SegemtTree(length + 1)
        for i, x in enumerate(_list):
            tmp.update(i + 1, x)
        return tmp

    @classmethod
    def built_from_list2(cls, _list):
        # length = len(_list)
        tmp = [0] * (len(_list) + 1)
        for i in range(0, len(_list)):
            i += 1
            tmp[i] += _list[i - 1]
            f = i + (i & (-i))
            if f <= len(_list):
                tmp[f] += tmp[i]
        a = SegemtTree(len(_list))
        a.tree = tmp
        return a

if __name__ == '__main__':
    t = SegemtTree.built_from_list2([1,2,3,-1,5,6,10])
    print(t.query_inter(1,5))
    t.update(1,3)
    print(t.query_inter(1,5))



