

def encrypt(s):
    l = []
    for i in s:
        x = ord(i) + 1
        z = chr(x)
        l.append(z)
    y = "".join(l)
    # print(y)
    f = y.encode("utf-8")
    # print(f)
    return f


def decrypt(s):
    f = s.decode("utf-8")
    # print(f)

    l = []
    for i in f:
        x = ord(i) - 1
        z = chr(x)
        l.append(z)
    y = "".join(l)
    return y
    # print(y)
