"""A module that manipulates lists."""

from time import sleep
from package.printer import *
from package.croupier import *

def total_column(lst, col):
	"""A function that calculates the sum of a column inside a list."""
	res = 0
	i = 0
	while i < len(lst):
		res += lst[i][col]
		i += 1
	return res

def find_idem(lst, answer, bet):
	"""A function that checks if an element isalready assigned inside list."""
	i = 0
	while i < len(lst):
		if lst[i][0] == answer:
			return True
		i += 1
	return False

def edit_idem(lst, answer, bet):
	"""A function that sees if an element is already assigned inside list
	and if so, adds the values to make one element.
	"""
	i = 0
	while i < len(lst):
		if lst[i][0] == answer: # if we find the value inside list
			lst[i][1] += bet
		i += 1

def del_bet(lang, honorific, p_bets, money, slp=0.5):
	"""A function that deletes bet chosen by the Player."""
	answer = None
	quit = False
	attempt = 0
	while not quit:
		attempt += 1
		print("\n")
		if attempt == 1: # Display only at first attempt
			if lang == "fr":
				mprint(" CROUPIER.— Très bien {}.\n".format(honorific))
			elif lang == "en":
				mprint(" CROUPIER.— Very well {}.\n".format(honorific))
			print("\n")
			sleep(slp)
		if lang == "fr":
			print1by1("Veuillez choisir dans la liste suivante l'élément à " \
			"supprimer :")
		elif lang == "en":
			print1by1("Please select from the following list the element " \
				"to delete:")
		print("\n")
		
		i = 0
		for i, elt in enumerate(p_bets):
			print1by1("{}. {} $  ==>  {}".format(i, p_bets[i][1], p_bets[i][0]))
			print("\n")
			i += 1
		
		sleep(slp)
		if lang == "fr":
			mprint("— Entrez q pour quitter —")
		elif lang == "en":
			mprint("— Enter q to quit —")
		print("\n\n")

		answer = input()
		
		if answer=="q" or answer=="Q": # If Player choose to quit
			quit = True
			break

		try: # Try conversion to int
			answer = int(answer)
		except:
			if lang == "fr":
				attempt_level(attempt, 
					"CROUPIER.— {}, je n'ai pas saisi...\n".format(honorific)) 
			elif lang == "en":
				attempt_level(attempt, 
					"CROUPIER.— {}, I didn't get that...\n".format(honorific)) 
			answer = False
			continue
		if answer<0 or answer>=len(p_bets):
			if lang == "fr":
				attempt_level(attempt, 
					"CROUPIER.— {}, l'un des éléments, s'il vous plaît !\n" \
					.format(honorific))
			elif lang == "en":
				attempt_level(attempt, 
					"CROUPIER.— {}, one of the elements, please !\n" \
					.format(honorific))
		else:
			money += p_bets[answer][1] # Give back bet money
			del p_bets[answer] # Delete chosen bet
			if lang == "fr":
				mprint(" CROUPIER.— {}, l'élément a bien été supprimé.\n" \
					.format(honorific))
			elif lang == "en":
				mprint(" CROUPIER.— {}, the element has been successfully " \
					"deleted.\n".format(honorific))
			# If list is empty, quit
			if not p_bets:
				quit = True
	return money
	
