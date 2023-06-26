#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        answer = fct(*args)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        answer = None
    return answer
