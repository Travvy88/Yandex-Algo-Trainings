f = open('input.txt', 'r')
d = int(f.readline())
x, y = map(int, f.readline().split())


def dist(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**-2


if d > 0 and 0 <= y <= -x + d and x >= 0:
    print(0)
elif d < 0 and 0 >= y >= -x + d and x <= 0:
    print(0)
elif d == 0 and x == 0 and y == 0:
    print(0)
else:
    a = dist(x, y, 0, 0)
    b = dist(x ,y, d, 0)
    c = dist(x, y, 0, d)

    if a >= b and a >= c:
        print(1)
    elif b >= a and b >= c:
        print(2)
    elif c >= b and c >= a:
        print(3)




f.close()
