"""A module that prints/arrange strings/numbers in a certain way"""

import os
import sys
import time

def print1by1(string, delay=0.008):
	"""A function that prints the string letter by letter."""
	for c in string:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(delay)
	print

def mprint(string):
	"""A function that prints strings at the middle of the terminal."""
	width = os.get_terminal_size().columns
	print(string.center(width))

def space_nb(nb):
	"""A function that seprates every 3 digits of the number."""
	nb = str(nb)
	
	if len(nb) > 3:		
		nbl = [str(c) for c in nb]
		res = []
		i = 1
		j = len(nb) - 1
		while i <= len(nb):
			if i%3==0 and i<len(nb):
				res.insert(0, " " + nbl[j])
			else:
				res.insert(0, nbl[j])
			i += 1
			j -= 1
		res = "".join(res)
		return res
	return nb

def sum_win(win1, win2, win4, win5, win6):
	"""A function that returns the sum of wins"""
	if not win1:
		win1 = 0
	if not win2:
		win2 = 0
	if not win4:
		win4 = 0
	if not win5:
		win5 = 0
	if not win6:
		win6 = 0
	return win1 + win2 + win4 + win5 + win6
