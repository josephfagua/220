

def encode(message, keyword):
    s = message
    k = keyword
    acc = " "
    k = k.upper()
    s = s.upper()
    s = s.split(" ")
    k = k.split(" ")
    s = "".join(s)
    k = "".join(k)
    for i in range(len(s)):
        c = s[i]
        key = k[i % len(k)]
        ord_c = ord(c) - 65
        ord_key = ord(key) - 65
        ck = (ord_key + ord_c) % 26
        cn = ck + 65
        ch = chr(cn)
        acc = acc + ch
    return acc


def main():

    print(encode("mama Te Quiero", "Te dije que te quiEro"))


if __name__ == '__main__':
    main()