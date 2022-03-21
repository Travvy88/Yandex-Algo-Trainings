f = open('input.txt', 'r')
n = int(f.readline())
events = []

for i in range(n):
    t, l = map(int, f.readline().split())
    events.append((t, 1))
    events.append((t + l, -1))

events.sort()
opened = 0
maxopened = 0

for x, t in events:

    if t == 1:
        opened += 1
    else:
        opened -= 1

    maxopened = max(opened, maxopened)

print(maxopened)
f.close()
