#!/usr/bin/python3
import dis
def magic_calculate(a, b):
	return (98 + a**b)
dis.dis(magic_calculate)
