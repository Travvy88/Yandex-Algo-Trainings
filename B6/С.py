f = open('cubroot.in', 'r')
a, b, c, d = map(int, input().split())


def equation(a, b, c, d, x):
    return a*x**3 + b*x**2 + c*x + d


def check(a, equation, m):
    if a > 0:
        return equation(a, b, c, d, m) >= 0
    else:
        return equation(a, b, c, d, m) <= 0


def fbinsearch(l, r, eps):
    while l + eps < r:
        m = (l + r) / 2
        if  check(a, equation, m):
            r = m
        else:
            l = m

    return l


print(fbinsearch(-1000, 1000, 0.0000001))
f.close()
