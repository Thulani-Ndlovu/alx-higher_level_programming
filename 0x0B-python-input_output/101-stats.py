#!/usr/bin/python3
"""Script definition"""


def print_stats(size, status_codes):
    """Prints the accumulated metrics."""
    print("File size: {}".format(size))
    for i in sorted(status_codes):
        print("{}: {}".format(i, status_codes[i]))


if __name__ == "__main__":
    import sys

    size = 0
    counter = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for Content in sys.stdin:
            if counter == 10:
                print_stats(size, status_codes)
                counter = 1
            else:
                counter += 1

            Content = Content.split()

            try:
                size += int(Content[-1])
            except (IndexError, ValueError):
                pass

            try:
                if Content[-2] in valid_codes:
                    if status_codes.get(Content[-2], -1) == -1:
                        status_codes[Content[-2]] = 1
                    else:
                        status_codes[Content[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
