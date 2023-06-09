#!/usr/bin/python3
def multiple_returns(sentence):
    info = ()
    if len(sentence) == 0:
        info = (len(sentence), None)
    else:
        info = (len(sentence), sentence[0])
    return (info)
