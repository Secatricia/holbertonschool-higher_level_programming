#!/usr/bin/python3
def uppercase(str):
    i = 0
    ch2 = ''
    while str[i:]:
        ch = ord(str[i])
        if ch > 96 and ch < 123:
            ch2 = chr(ch-32)
            print(ch2, end="")
        else:
            print(str[i], end="")
        i += 1
    print("")
