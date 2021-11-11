def vigenere():
    s = eval(input("enter message to encode"))
    k = eval(input("enter key"))
    acc = " "
    k = k.upper()
    s = s.upper()
    s = s.split(" ")
    k = k.split(" ")
    s = "".join(s)
    k = "".join(k)
    print(k)
    for i in range(len(s)):
        c = s[i]
        print(c)
        key = k[i % len(k)]
        print(key)
        ord_c = ord(c)-65
        print(ord_c)
        ord_key = ord(key)-65
        print(ord_c, ord_key)
        ck = (ord_key + ord_c) % 26
        print(ck)
        cn = ck + 65
        ch = chr(cn)
        print(ch)
        acc = acc + ch
    print(acc)


vigenere()
        