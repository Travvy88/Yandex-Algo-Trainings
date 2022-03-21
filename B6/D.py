f = open('input.txt', 'r')
a, k, b, m, x = map(int, f.readline().split())


def lbinsearch(a, k, b, m, x):
    l = 0
    r = x*2
    while l < r:
        mid = (l + r) // 2
        trees = a * (mid  - mid // k) + b * (mid  - mid // m)
        if trees >= x:
            r = mid
        else:
            l = mid + 1

    return l


print(lbinsearch(a, k, b, m, x))

f.close()
