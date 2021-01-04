
def check(mid):
    return

def bs_1(l, r):
    while l < r:
        mid = l + r >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    return l

def bs_2(l, r):
    while l < r:
        mid = (l + r + 1) >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    return l

# 查找元素的上下界
# bisect模块
# 查找元素的左边界
def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

        The return value i is such that all e in a[:i] have e < x, and all e in
        a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
        insert just before the leftmost x already there.

        Optional args lo (default 0) and hi (default len(a)) bound the
        slice of a to be searched.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo +hi) >> 1
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


# 查找元素的上边界
def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

        The return value i is such that all e in a[:i] have e <= x, and all e in
        a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
        insert just after the rightmost x already there.

        Optional args lo (default 0) and hi (default len(a)) bound the
        slice of a to be searched.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] > x:
            hi = mid
        else:
            lo = mid + 1
    return lo
