f = open('input.txt', 'r')
n = int(f.readline())
events = []

for i in range(n):
    l, r = map(int, f.readline().split())
    events.append((l, -1))
    events.append((r, 1))

events.sort()
opened = 0
start = events[0][0]
result = 0

for x, t in events:
    if start == -1:
        start = x
    if t == -1:
        opened += 1
    else:
        opened -= 1

    if opened == 0:
        result += x - start
        start = -1

print(result)
f.close()
