f = open('input.txt', 'r')
n = int(f.readline())
d = dict()
for i in range(n):
    color, number = map(int, f.readline().split())

    if color not in d.keys():
        d[color] = number
    else:
        d[color] += number

colors = sorted(d.keys())
for color in colors:
    print(color, d[color])

    
f.close()
