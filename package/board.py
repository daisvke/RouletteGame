"""A module that keeps informing of the current state."""

import time
from package.printer import *
from package.color import *

def rest(money):
	"""A function that displays the remaining money."""
	print("\n")
	print("================================")
	print("\033[93m CASH: {0} $\033[0m".format(space_nb(money)))
	print("================================")
	print("\n")

def bet_reg(p_bets, delay=1):
	"""A function that displays how much the Player bet on what number(s)."""
	time.sleep(delay)
	i = 0
	bet = 0
	what = 0
	space = ""
	while i < len(p_bets):
		count = 0
		space = ""
		if i+1 < len(p_bets): # If not the last element, put 2 elts
			bet = p_bets[i][1] # bet of first bet
			bet2 = p_bets[i + 1][1] # second bet
			# The first element
			if type(p_bets[i][0]) is int: # If first elt is int 
				if p_bets[i][0] == 0: # If number is zero, print in green bg
					what = "\u001b[42m 0  \u001b[40m"
					count += 1
				else:
					what = p_bets[i][0]
			else: # Or string (ex: color, pair, low bet)
				if p_bets[i][0] == "ROUGE": # If elt is red, print in red
					what = "\u001b[41m " + p_bets[i][0] + " \u001b[40m"
					count += 1
				else:
					what = p_bets[i][0]

			# The second bet
			if type(p_bets[i + 1][0]) is int: # If first elt is int 
				if p_bets[i + 1][0] == 0: # If number is zero, print in green bg
					what2 = "\u001b[42m 0 \u001b[40m"
					count += 1
				else:
					what2 = p_bets[i + 1][0]
			else: # Or string (ex: color, pair, low bet)
				if p_bets[i + 1][0] == "ROUGE": # If elt is red, print in red
					what2 = "\u001b[41m " + p_bets[i + 1][0] + " \u001b[40m"
					count += 1
				else:
					what2 = p_bets[i + 1][0]
			# Define space to compensate coloring that decenters text
			if count == 0:
				space = "         "
			if count == 1:
				space = "                    "
			if count == 2:
				space = "                             "

			if i == 0:
				mprint("          \033[93m" \
					"⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\033[0m")
			mprint("{4}{0} $ => {1}  \033[93m⋮\033[0m  {2} $ => {3}".format(space_nb(bet), \
				what, space_nb(bet2), what2, space)) 
			mprint("          \033[93m" \
				"⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\033[0m")
			i += 2

		else: # If last element, display in the middle
			bet = p_bets[i][1]
			if type(p_bets[i][0]) is int:
				if p_bets[i][0] == 0: # If number is zero, print in green bg
					what = "\u001b[42m 0 \u001b[40m"
					space = "         " # Space to compensate &keep centered
				else:
					what = p_bets[i][0]
			else:
				if p_bets[i][0] == "ROUGE": # If elt is red, print in red
					what = "\u001b[41m " + p_bets[i][0] + " \u001b[40m"
					space = "         "
				else:
					what = p_bets[i][0]
			if i == 0:
				mprint("          \033[93m" \
					"⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\033[0m")
			mprint(" {}{} $ => {}".format(space, space_nb(bet), what)) 
			mprint("          \033[93m" \
					"⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\033[0m")
			i += 1
	mprint("\n")
	time.sleep(delay)

def nspin(nbr, op, max=36):
	"""A function that makes numbers spin with the roulette
	and not go negative/beyond max number.
	"""
	if nbr+op < 0:
		return (max + nbr + op + 1)
	elif nbr+op > max:
		return (nbr + op - max -1)
	else:
		return (nbr + op)

def colored_list(nbr, i=-21, max=1):
	"""A function that works with spin()
	
	It puts colored numbers into a dictionary according
	to the roulette numbers' color patterns.
	The index represents the distance from the roulette number.
	"""
	# If the number is red, print it in red !
	# We create a dict of numbers that has bg colored in red, if needed
	nb_clr = define_nb_clr() # Import list containing colors of numbers
	clr_lst = {}
	while i <= max:
		if nb_clr[nspin(nbr, i)] == "rouge":
			str_nb = str(nspin(nbr, i))
			clr_lst[i] = "\u001b[41m " + str_nb + " \u001b[40m"
		elif nb_clr[nspin(nbr, i)] == "vert": # If number is zero
			str_nb = str(nspin(nbr, i))
			clr_lst[i] = "\u001b[42m " + str_nb + " \u001b[40m"
		else:
			clr_lst[i] = nspin(nbr, i)
		i += 1
	return clr_lst

def space(r_number, ex_r_number, nb1, nb2, nb3, ctype="colored"):
	"""A function that works with spin and defines space length to compensate 
	and makes centered text possible.

	There are 11 spaces to move to compensate for each of the two fisrt 
	color settings.
	"""
	if ctype == "colored":
		colored = colored_list(r_number)
		lst = [colored[nb1], colored[nb2], colored [nb3]]
	else:
		colored_ex = colored_list(ex_r_number)
		lst = [colored_ex[nb1], colored_ex[nb2], colored_ex[nb3]]
	counter = 0

	# Check number of colored numbers, which will determine space to add
	i = 0
	while i < len(lst):
		if type(lst[i]) is not int:
			counter += 1
		i += 1
	if counter == 2:
		return "                      "
	if counter == 3:
		return "                               "
	return "           "


def spin(r_number, ex_r_number, p_bets):
	"""A function that displays the roulette spining according to time."""
	# Get list of bg colored numbers that result from nspin
	colored = colored_list(r_number)
	colored_ex = colored_list(ex_r_number)

	mprint(" CROUPIER.— Les jeux sont faits...")
	mprint("\n")
	# State 0	
	mprint("RIEN...")
	mprint("\n")
	mprint("-----∀")
	mprint("__________________")
	mprint("{3}{0} | {1} | {2}\n".format(colored_ex[-1], colored_ex[0], 
	colored_ex[1], space(r_number, ex_r_number, -1, 0, 1, "ex")))
	mprint("\n")
	time.sleep(1)
	# State 1
	mprint("NE...")
	mprint("\n")
	mprint("--------∀")
	mprint("__________________")
	mprint("{3}{0} | {1} | {2}\n".format(colored[-21], colored[-20],
	colored[-19], space(r_number, ex_r_number, -21, -20, -19)))
	mprint("\n")
	bet_reg(p_bets)
	# State 2
	mprint("VA...")
	mprint("\n")
	mprint("-----------∀")
	mprint("__________________")
	mprint("{3}{0} | {1} | {2}\n".format(colored[-11], colored[-10],
	colored[-9], space(r_number, ex_r_number, -11, -10, -9)))
	mprint("\n")
	time.sleep(1)
	# State 3
	mprint("PLUS !!!")
	mprint("\n")
	mprint("--------∀")
	mprint("__________________")
	mprint("{3}{0} | {1} | {2}\n".format(colored[-6], colored[-5],
	colored[-4], space(r_number, ex_r_number, -6, -5, -4)))
	mprint("\n")
	bet_reg(p_bets)
	# State 4
	mprint("---∀")
	mprint("__________________")
	mprint("{3}{0} | {1} | {2}\n".format(colored[-4], colored[-3],
	colored[-2], space(r_number, ex_r_number, -4, -3, -2)))
	mprint("\n")
	time.sleep(1.5)
	# State 5
	mprint("∀")
	mprint("__________________")
	mprint("{3}{0} | {1} | {2}\n".format(colored[-1], colored[0],
	colored[1], space(r_number, ex_r_number, -1, 0, 1)))
	mprint("\n")
	time.sleep(1)

