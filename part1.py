def func1p1(a, k):
    if a & (2 ** (k - 1)):
        return 1
    else:
        return 0
    #return a & (2 ** (k - 1))


def func1p2(a, k, f):
    if f:
        return a | (2 ** (k - 1))
    else:
        return a & ~(2 ** (k - 1))


def func1p3(a, i, j):
    if func1p1(a, i) == func1p1(a, j):
        return a
    else:
        a = func1p2(a, i, func1p1(a, i) == 0)
        a = func1p2(a, j, func1p1(a, j) == 0)
        return a


def func1p4(a, m):
    return (a >> m) << m


def func2a(a, i, len):
    if i > len:
        return 0
    mask = ~((-1) << len) >> i << i
    temp1 = (a & mask) >> (len - i) << i
    temp2 = a & ~mask
    return temp1 | temp2


def func2b(a, i, len):
    if i > len:
        return 0
    mask = ~((-1) << (len - i)) & ((-1) << i)
    return (a & mask) >> i

# print(func1p1(5, 2))
# print(func1p1(5, 1))
#
#
# a = 5
# a = func1p3(a, 1, 2)
# print(a)
#
# print(func1p4(23, 2))
#
# print(func2a(2285, 3, 12))
# print(func2b(2285, 3, 12))

