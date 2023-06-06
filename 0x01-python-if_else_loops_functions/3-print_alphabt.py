#!/usr/bin/python3
for i in range(97, 123):
    if (str(chr(i)) != 'q') and (str(chr(i)) != 'e'):
        print('{}'.format(str(chr(i))), end="")
