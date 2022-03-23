from math import pi

f = open('input.txt', 'r')
n = int(f.readline())
events = []
events_left = []
events_right = []
for i in range(n):
    r1, r2, ph1, ph2 = map(float, f.readline().split())
    if ph1 > ph2:
        events.append((ph2, -1, r1, r2))
        events.append((ph1 + 2*pi, 1, r1, r2))
    else:
        events.append((ph1, -1, r1, r2))
        events.append((ph2, 1, r1, r2))
        events.append((ph1 + 2*pi, -1, r1, r2))
        events.append((ph2 + 2*pi, 1, r1, r2))


events.sort()

opened = 0
result = 0
i = 0
lastopened = False
while i < len(events):
    event = events[i]
    if event[1] == -1:
        opened += 1
        lastopened = event
    else:
        if opened == n:
            rr = [event[2], event[3], lastopened[2], lastopened[3]]
            rr.sort()
            r1, r2 = rr[1], rr[2]
            ph1, ph2 = lastopened[0], event[0]
            result += (ph2 - ph1) * (r2 ** 2 - r1 ** 2) / 4
        opened -= 1
    i += 1

print(result)
f.close()
