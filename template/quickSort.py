
def quickSort(arr, l, r):
    if l >= r:
        return
    i, j = l - 1, r + 1
    x = arr[l + r >> 1]
    while i < j:
        while True:
            i += 1
            if arr[i] >= x:
                break
        while True:
            j -= 1
            if arr[j] <= x:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i],
    quickSort(arr, l, j)
    quickSort(arr, j + 1, r)

if __name__ == '__main__':
    arr = [1,9,4,8,3]
    quickSort(arr, 0, len(arr) - 1)
    print(arr)
