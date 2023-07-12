#!/usr/bin/python3
'''Function definition'''


def append_after(filename="", search_string="", new_string=""):
    '''
        inserts a line of text to a file, after each
        line containing a specific string
    '''
    info = ""
    with open(filename) as r:
        for Content in r:
            info += Content
            if search_string in info:
                info += new_string
    with open(filename, "w") as w:
        w.write(info)
