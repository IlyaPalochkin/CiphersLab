import math
import part1


def func4(n):
    return math.log(n & (-n), 2)


def func5(n):
    x = 1
    p = -1
    while x < n:
        x <<= 1
        p += 1
    return p


def func6(n):
    tmp = n & 1
    while n:
        n >>= 1
        tmp ^= (n & 1)
    return tmp & 1


def right_shift(n, k, p):
    return (n >> k) | (n << (p - k))


def left_shift(n, k, p):
    return (n << k) | (n >> (p - k))


def func8(n, m):
    x = 0
    for i in range(len(m)):
        x = x | (part1.func1p1(n, m[i] + 1) << (len(m) - i - 1))
    return x


print(func4(62))
print(func5(16))
print(func6(231))
print(func8(11, [1, 0, 3, 2]))
