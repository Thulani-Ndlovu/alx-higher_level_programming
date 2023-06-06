#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            c = str[i]
            c = ord(c)
            c = c - 32
            c = chr(c)
            str = str[:i] + c + str[i+1:]
        print('{}'.format(str[i]), end="")
    print("\n")
