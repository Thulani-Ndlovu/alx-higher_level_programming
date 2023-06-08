#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    tally = 0
    if (sys.argv) == 1:
        print(tally)
    else:
        for i in range(1, len(sys.argv)):
            tally += int(sys.argv[i])
        print('{}'.format(tally))
