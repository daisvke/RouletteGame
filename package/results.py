"""A module that manage the consequences of the roulette's results"""

from time import sleep
import sys
from math import ceil
from package.printer import *
from package.board import *
from package.player import *

def results(lang, last_name, honorific, p_bets, money, 
		r_number, r_color, r_parity, r_lowhigh, 
		slp=0.5):
	"""A function that prints roulette's results accordgin to the situation."""
	i = 0
	s1 = s2 = s3 = s4 = s5 = s6 = False
	win1 = win2 = win4 = win5 = win6 = 0
	gain = 0 # Money gained by Player each turn

	while i < len(p_bets):
		# Money gained for each winning bet
		if type(p_bets[i][0]) is int: # if bet elt is int
			if p_bets[i][0] == r_number:
				if r_number == 0: # If zero
					money += ceil(p_bets[i][1] * 50)
					win1 = ceil(p_bets[i][1] * 49)
					s1 = True
				elif p_bets[i][0] != 0: # Other numbers
					money += ceil(p_bets[i][1] * 35)
					win2 = p_bets[i][1] * 34
					s2 = True
			else: # If Player's nbr was very close
				if p_bets[i][0]==nspin(r_number, -2) or \
						p_bets[i][0]==nspin(r_number, 2) or \
						p_bets[i][0]==nspin(r_number, -1) or \
						p_bets[i][0]==nspin(r_number, 1):
					s3 = True
		else: # If bet elt is str (ex: color or parity)
			if p_bets[i][0] == r_color:
				money += ceil(p_bets[i][1] * 2)
				win4 = p_bets[i][1]
				s4 = True
			elif p_bets[i][0] == r_parity:
				money += ceil(p_bets[i][1] * 2)
				win5 = p_bets[i][1]
				s5 = True
			elif p_bets[i][0] == r_lowhigh:
				money += ceil(p_bets[i][1] * 2)
				win6 = p_bets[i][1]
				s6 = True
		i += 1

	# gain is the sum of all wins
	gain = sum_win(win1, win2, win4, win5, win6)
	space = space0 = ""
	
	if gain > 0:
		if r_color == "ROUGE": # If color is red, print in red
			r_color = "\u001b[41m ROUGE \u001b[40m"
			space = "          "
		if r_number == 0: # If zero, print in green
			r_number = "\u001b[42m 0 \u001b[40m"
			space0 = "          "

		mprint("          " \
			"\033[93m∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧ GAIN ∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧\n\033[0m")
		if s1:
			mprint("{}{}   ==>   x 50   =   {} $\n"\
				.format(space0, r_number, space_nb(win1)))
			sleep(slp)
		if s2:
			mprint("{}   ==>   x 35   =   {} $\n"\
				.format(r_number, space_nb(win2)))
			sleep(slp)
		if s4:
			mprint("{}{}   ==>   x 1   =   {} $\n"\
				.format(space, r_color, space_nb(win4)))
			sleep(slp)
		if s5:
			mprint("{}   ==>   x 1   =   {} $\n"\
				.format(r_parity, space_nb(win5)))
			sleep(slp)
		if s6:
			mprint("{}   ==>   x 1   =   {} $\n"\
				.format(r_lowhigh, space_nb(win6)))
		mprint("         " \
			"\033[93m∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧∨∧\033[0m")
		print("\n\n")

		# Now we print comments concerning the results
		if s1:
			if lang == "fr":
				mprint(" CROUPIER.— C'est incroyable, toutes mes " \
					"félicitations, {} !\n".format(honorific))
				sleep(slp)
				mprint(" Le zéro tombe si rarement,\n")
				sleep(slp)
				mprint(" ce n'est pas tous les jours que je vois cela !")
			elif lang == "en":
				mprint(" CROUPIER.— This is incredible, congratulations, " \
					"{} !\n".format(honorific))
				sleep(slp)
				mprint(" The zero comes so rarely,\n")
				sleep(slp)
				mprint(" It is not everyday that I can see that !")
			print("\n")
		elif s2 or s4 or s5 or s6:
			if lang == "fr":
				mprint(" CROUPIER.— Bravo {} !\n".format(honorific))
				sleep(slp)
				mprint(" Cela vous fait un gain total de {} $ !\n"\
					.format(space_nb(gain)))
			elif lang == "en":
				mprint(" CROUPIER.— Bravo {} !\n".format(honorific))
				sleep(slp)
				mprint(" You have a total gain of {} $ !\n"\
					.format(space_nb(gain)))
	elif gain==0 and len(p_bets)>0: # No gain = no congratulations
		if money > 0:
			if lang == "fr":
				mprint(" CROUPIER.— C'est dommage !\n")
			elif lang == "en":
				mprint(" CROUPIER.— It's a shame !\n")
			sleep(slp)
		if s3:
			if lang == "fr":
				mprint(" Vous étiez si proche pour le {} !\n".format(r_number))
			elif lang == "en":
				mprint(" You were so close for the {} !\n".format(r_number))
			sleep(slp)
		if money > 0:
			if lang == "fr":
				mprint(" Vous ferez mieux la prochaine fois, {} {} !\n" \
					.format(edit_honor(lang, honorific), last_name))
				sleep(slp)
				mprint(" J'en suis certain !\n")
			elif lang == "en":
				mprint(" You will do better next time, {} {} !\n" \
					.format(edit_honor(lang, honorific), last_name))
				sleep(slp)
				mprint(" I am sure of it !\n")
		if money == 0:
			if lang == "fr":
				mprint(" CROUPIER.— Je suis navré pour votre perte, {}...\n"\
					.format(honorific)) 
			elif lang == "en":
				mprint(" CROUPIER.— I am sorry for your loss, {}...\n"\
					.format(honorific)) 

	return money	

