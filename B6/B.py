f = open('input.txt', 'r')
n = int(f.readline())
array = list(map(int, f.readline().split()))  # sorted
m = int(f.readline())
numbers = list(map(int, f.readline().split()))


def lbinsearch(array, number):
    l = 0
    r = len(array) - 1
    while l < r:
        m = (l + r) // 2
        if array[m] >= number:
            r = m
        else:
            l = m + 1

    return l + 1


def rbinsearch(array, number):
    l = 0
    r = len(array) - 1
    while l < r:
        m = (l + r + 1) // 2
        if array[m] <= number:
            l = m
        else:
            r = m - 1
    return l + 1


for number in numbers:
    if number not in array:
        print(0, 0)
    else:
        print(lbinsearch(array, number), rbinsearch(array, number) )

f.close()
