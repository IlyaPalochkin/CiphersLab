
def bit_generator(key):
    res = []
    for char in key:
        res.append(convert(bin(ord(char))[-4:]))
        res.append(convert(invert(bin(ord(char))[-4:])))
    return set(res)


def convert(arr):
    return "".join(str(i) for i in arr)


def invert(arr):
    res = []
    for char in arr:
        if char == '1':
            res.append(0)
        else:
            res.append(1)
    return res


def invert_to_array(tmp):
    res = []
    for char in tmp:
        res.append(int(char))
    return res


def to_binary(plain):
    s = ""
    i = 0
    for i in plain:
        binary = str(' '.join(format(ord(x), 'b') for x in i))
        # binary = bin(ord(i))
        j = len(binary)
        while (j < 8):
            binary = "0" + binary
            j = j + 1
        s = s + binary
    binary_values = []
    k = 0
    while k < len(s):
        binary_values.insert(k, int(s[k]))
        k = k + 1
    return s


def xor(str1, str2):
    res = ''
    for ch1, ch2 in zip(str1, str2):
        if ch1 == ch2:
            res += '1'
        else:
            res += '0'
    return res


def convert_binary_to_str(binary):
    s = ""
    length = len(binary) - 4
    i = 0
    while i <= length:
        s = s + chr(int(binary[i:i + 8], 2))
        i = i + 8
    return str(s)


def part31(txt, key):
    # fi = open('txto.txt', 'r')
    # fo = open('txt.txt', 'w')
    # txt = to_binary(fi.read())

    bits = bit_generator(key)
    length = len(txt) - 4
    i = 0
    res = ''
    while i <= length:
        if txt[i:i+4] in bits:
            res += convert(invert(txt[i:i+4]))
        else:
            res += convert(txt[i:i+4])
        i += 4

    return convert_binary_to_str(res)
    # fo.write(convert_binary_to_str(res))
    # fo.close()


def vernam(txt, key):
    if len(txt) % len(key) != 0:
        print('Wrong key')
        return 0

    i = 0
    res = ''
    while i <= len(txt) - len(key):
        res += xor(txt[i:i + len(key)], key)
        i += len(key)
    return convert_binary_to_str(res)


fi = open('txto.txt', 'r')
fo = open('txt.txt', 'w')
txt = to_binary(fi.read())

fo.write(vernam(txt, to_binary('Nado 11 sym')))

fo.close()
fi.close()
