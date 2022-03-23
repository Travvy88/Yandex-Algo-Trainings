from math import pi

f = open('input.txt', 'r')
n = int(f.readline())
events = []

for i in range(n):
    r1, r2, ph1, ph2 = map(float, f.readline().split())
    if ph1 > ph2:
        unopened = 1
    else:
        unopened = 0

    events.append((ph1, -1, r1, r2, unopened))
    events.append((ph2, 1, r1, r2, unopened))

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
    elif event[-1] == 1:
        if lastopened:
            events.append((lastopened[0], lastopened[1],lastopened[2],lastopened[3], 2))
        else:
            events.append((0, event[1],event[2],event[3], 2))
        events.append((event[0], event[1],event[2],event[3], 2))  # if 2 then it opened but
    else:
        if opened == n:
            rr = [event[2], event[3], lastopened[2], lastopened[3]]
            rr.sort()
            r1, r2 = rr[1], rr[2]
            ph1, ph2 = lastopened[0], event[0]
            if event[4] == 2:
                result += (2*pi - ph1) * (r2**2 - r1**2) / 2
                result += ph1 * (r2**2 - r1**2) / 2
            else:
                result += (ph2 - ph1) * (r2**2 - r1**2) / 2
        opened -= 1
    i += 1

print(result)
f.close()
