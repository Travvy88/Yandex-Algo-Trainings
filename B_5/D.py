f = open('input.txt', 'r')
s = f.readline()
first = 0
second = 0

while first < len(s) and second < len(s):
    if s[first] == '(' and s[second] == ')':
        first += 1
        second += 1
    elif s[first] == '(' and s[second] != ')':
        second += 1
    elif s[first] != '(' and s[second] == ')':
        first += 1

f.close()