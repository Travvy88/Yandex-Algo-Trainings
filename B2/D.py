f = open('input.txt', 'r')
l, k = map(int, f.readline().split())
mas = list(map(int, f.readline().split()))


def fun(l, k, mas):
    if k == 1:
        return mas[0]
    mid_bench = int(l / 2)
    odd = l % 2 != 0
    idx = 0
    for i in range(k):
        if mas[i] < mid_bench:
            idx = i
        elif mas[i] == mid_bench:
            if odd:
                return [mas[i]]
            else:
                return mas[idx], mas[i]
        else:
            return mas[idx], mas[i]



out = fun(l, k, mas)
if len(out) == 1:
    print(out[0])
else:
    print(out[0], out[1])
f.close()
