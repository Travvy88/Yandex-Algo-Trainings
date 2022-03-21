f = open('input.txt', 'r')
n, k = map(int, f.readline().split())
array = list(map(int, f.readline().split()))
sorted_array = sorted(array)

def Kcheck(k, l, array):
    start = array[0]
    used = 1
    for num in array:
        if num - start > l:
            used += 1
            start = num
            if used > k:
                return 0
    return used <= k


def lbinsearch(array, k):
    l = 0
    r = array[-1]
    while l < r:
        m = (l + r) // 2

        if Kcheck(k, m, array):
            r = m
        else:
            l = m + 1

    return l
min_num = sorted_array[0] - 1
sorted_array = [num - min_num for num in sorted_array]
print(sorted_array)
print(lbinsearch(sorted_array, k))
f.close()
