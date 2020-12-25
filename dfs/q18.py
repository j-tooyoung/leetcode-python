def check(n, pre, log, square):
    if len(log) == n:
        if (1 + pre) in square:
            print(log)
            return True
    else:
        for i in range(1, n + 1):
            if i in log:
                continue
            if ((i + pre) in square) and check(n, i, log + [i], square):
                return True
    return False


if __name__ == '__main__':
    n = 2
    while True:
        square = [i * i for i in range(1, n)]
        if check(n, 1, [1], square):
            print(n)
            break
        n += 1
