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


def rbinsearch(array, number):
    l = 0
    r = len(array) - 1
    while l < r:
        m = (l + r + 1) // 2
        if array[m] <= number:
            l = m
        else:
            r = m - 1
    return l + 1


f = open('input.txt', 'r')
n, m = map(int, f.readline().split())
kitties = list(map(int, f.readline().split()))
kitties.sort()
mx = max(kitties)
mn = min(kitties)

for i in range(m):
    l, r = map(int, f.readline().split())
    if (l < mn and r < mn) or (l > mx and r > mx):
        print(0)
    else:
        # print(rbinsearch(kitties, r), lbinsearch(kitties, l))
        print(rbinsearch(kitties, r) - lbinsearch(kitties, l), end=' ')


f.close()