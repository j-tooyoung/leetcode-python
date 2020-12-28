N = 1000006

tmp = [0] * N
def mergeSort(arr, l , r):
    if l >= r:
        return
    mid = l + r >> 1
    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    i, j, k = l, mid + 1, 0
    while i <= mid and j <= r:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            k += 1
            i += 1
        else:
            tmp[k] = arr[j]
            k += 1
            j += 1
    while i <= mid:
        tmp[k] = arr[i]
        k += 1
        i += 1
    while j <= r:
        tmp[k] = arr[j]
        k += 1
        j += 1
    i,  k = l, 0
    while i <= r:
        arr[i] = tmp[k]
        k += 1
        i += 1


if __name__ == '__main__':
    arr = [1, 9, 4, 8, 3]
    mergeSort(arr, 0, len(arr) - 1)
    print(arr)
