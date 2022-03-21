f = open('input.txt', 'r')
n = int(f.readline())
array = list(map(int, f.readline().split()))
array.sort()
k = int(f.readline())


def lbinsearch(array, L):
    l = 0
    r = len(array) - 1
    while l < r:
        m = (l + r) // 2
        if array[m] >= L:
            r = m
        else:
            l = m + 1

    return l


def rbinsearch(array, R):
    l = 0
    r = len(array) - 1
    while l < r:
        m = (l + r + 1) // 2
        if array[m] <= R:
            l = m
        else:
            r = m - 1
    return l


for i in range(k):
    l, r = map(int, f.readline().split())
    if (l > array[-1] and r > array[-1]) or (l < array[0] and r < array[0]):
        print(0, end=' ')
    else:
        print(rbinsearch(array, r) - lbinsearch(array, l) + 1, end=' ')



f.close()