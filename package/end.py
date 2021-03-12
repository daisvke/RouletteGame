"""A module that says goodbye in a nice way."""

from time import sleep
import json
from package.printer import *
from package.croupier import *
from package.player import *

def bye(t_start, lang, money, full_name, player):
	"""A function that saves modified data of Player, with save(), then
	says goodbye to the Player, followed by logo.
	"""
	save(t_start, money, full_name, player) # Save data
	
	print("\n\n\n")
	if lang == "fr":
		mprint("À bientôt !")
	elif lang == "en":
		mprint("See you !")
	print("\n\n")
	sleep(1)
	mprint(" RINO\n")
	mprint(" — Minimal Casinos —\n")
	print("\n\n\n")

def stay_leave(t_start, lang, honorific, full_name, player, 
		p_gain, start_money, money, slp=0.5):
	"""A function that asks if the Player wants to stay/leave."""
	sleep(1.5)
	attempt = 0
	if full_name:
		lst = []
		lst = full_name.split(".") # Get the last name from string
		last_name = lst[0] 
	else:
		last_name = "Guest"

	answer = None
	play = 0
	while not answer:
		attempt += 1
		if lang == "fr":
			print1by1("CROUPIER.— Vous restez avec nous, {} ? (y/n)"\
			.format(honorific))
		elif lang == "en":
			print1by1("CROUPIER.— Are you staying with us, {} ? (y/n)"\
			.format(honorific))
		print("\n\n")
		sleep(slp)
		answer = input()
		if answer=="y" or answer=="Y":
			answer = 1
		elif answer=="n" or answer=="N" :
			answer = 2
			if money >= 500:
				if lang == "fr":
					mprint(" Vous allez nous manquer, {} {} !\n"\
						.format(edit_honor(lang, honorific), last_name))
				elif lang == "en":
					mprint(" We will miss you, {} {} !\n"\
						.format(edit_honor(lang, honorific), last_name))
				if p_gain > start_money*5:
					sleep(slp)
					if lang == "fr":
						mprint(" Toutes mes félicitations !\n")
					elif lang == "en":
						mprint(" Congratulations !\n")
				bye(t_start, lang, money, full_name, player)
			if money < 500:	
				sleep(slp)
				if lang == "fr":
					mprint(" Navré de vous voir partir, {} {} !\n"\
						.format(edit_honor(lang, honorific), last_name))
				elif lang == "en":
					mprint(" Sorry to see you go, {} {} !\n"\
						.format(edit_honor(lang, honorific), last_name))
				bye(t_start, lang, money, full_name, player)
		else:
			answer = None
			if lang == "fr":
				attempt_level(attempt, lang, honorific, \
					"CROUPIER.— {}, soit vous restez, " \
					"soit vous continuez...!\n".format(honorific))
			elif lang == "en":
				attempt_level(attempt, lang, honorific, \
					"CROUPIER.— {}, you either stay, " \
					"or leave...!\n".format(honorific))
		play = answer

		return play


