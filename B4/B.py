f = open('input.txt', 'r')

d = dict()
inp = f.readline()

while inp:
    name, votes = inp.split()
    votes = int(votes)

    if name not in d.keys():
        d[name] = votes
    else:
        d[name] += votes
    inp = f.readline()

names = sorted(d.keys())
for name in names:
    print(name, d[name])

f.close()
