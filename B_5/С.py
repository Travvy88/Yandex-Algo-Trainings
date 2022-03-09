f = open('input.txt', 'r')
n, m = map(int, f.readline().split())
groups = list(map(int, f.readline().split()))
rooms = list(map(int, f.readline().split()))

g = []
r = []
for i in range(len(groups)):
    g.append((groups[i], i))
for i in range(len(rooms)):
    r.append((rooms[i], i))

sortedrooms = sorted(r)
sortedgroups = sorted(g)

gpointer = 0
rpointer = 0
cnt = 0
schedule = [0] * n

while gpointer < len(g) and rpointer < len(r):
    group = sortedgroups[gpointer]
    room = sortedrooms[rpointer]

    if group[0] + 1 <= room[0]:
        schedule[group[1]] = room[1] + 1
        gpointer += 1
        rpointer += 1
        cnt += 1

    elif group[0] + 1 > room[0]:
        rpointer += 1

print(cnt)
print(*schedule)

f.close()