f = open('input.txt', 'r')

a, b, c, d = map(int, f.read().split())
x = 0
if a == 0 and b == 0:
    print('INF')

elif a == 0:
    print('NO')

else:
    x = - b / a
    if c*x + d == 0:
        print('NO')
    elif -b % a == 0:
        print(int(x))
    else:
        print('NO')


f.close()