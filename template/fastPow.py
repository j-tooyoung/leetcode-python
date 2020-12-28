
def fastPow(a, b, p):
    res = 1
    while b:
        if b & 1:
            res = res * a % p
        a = a * a % p
        b >>= 1
    return res


    return

if __name__ == '__main__':
    print(fastPow(1,3,5))
    print(fastPow(2,3,5))
    print(fastPow(2,14,5))




