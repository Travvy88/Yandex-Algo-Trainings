f = open('input.txt', 'r')
lines = f.read().split('\n')


data = dict()
# data[party] = [votes, men, stage2]
summa = 0
for line in lines:
    if line == '':
        continue
    line = line.split()
    votes = int(line[-1])
    summa += votes
    name = ''
    for n in line[:-1]:
        name += f'{n} '

    data[name[:-1]] = [votes, 0, 0]

men_sum = 0
pich = summa / 450
for party in data.keys():
    votes, men, stage2 = data[party]
    new_men = int(votes // pich)
    stage2 = (votes / pich) % 1
    data[party][1] = new_men
    data[party][2] = stage2
    men_sum += new_men


if men_sum < 450:
    new_data = dict(sorted(data.items(), reverse=True, key=lambda x: (x[1][2], x[1][0])))

    for i, key in zip(range(450 - men_sum), new_data.keys()):
        new_data[key][1] += 1
    for key in data.keys():
        print(key, new_data[key][1])
else:
    for key in data.keys():
        print(key, data[key][1])

f.close()
