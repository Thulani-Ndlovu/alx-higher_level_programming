#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) > 0:
        Numerator = 0
        Denominator = 0
        for x in my_list:
            Numerator += x[0] * x[1]
            Denominator += x[1]
        return Numerator / Denominator
    return 0
