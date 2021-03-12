"""A module that works with the answers the Player gives."""

from package.printer import *

def find_bet_option(answer):
	"""A function that checks if answer exists as an option."""
	if type(answer) is str:
		if answer=="r" or answer=="R": 
			return True
		elif answer=="b" or answer=="B":
			return True
		elif answer=="o" or answer=="O":
			return True
		elif answer=="e" or answer=="E":
			return True
		elif answer=="m" or answer=="M":
			return True
		elif answer=="p" or answer=="P":
			return True
	return False

def edit_bet_option(answer):
	"""A function that checks if the answer is a string,
	and if so, to what bet option it corresponds,
	then returns its value.
	"""
	if type(answer) is str:
		if answer=="r" or answer=="R": 
			answer = "ROUGE"
			print("\n")
			mprint("           === \u001b[41m ROUGE / RED \u001b[40m ===")
		elif answer=="b" or answer=="B":
			answer = "NOIR"
			print("\n")
			mprint("=== NOIR / BLACK ===")
		elif answer=="o" or answer=="O":
			answer = "PAIR"
			print("\n")
			mprint("=== PAIR / EVEN ===")
		elif answer=="e" or answer=="E":
			answer = "IMPAIR"
			print("\n")
			mprint("=== IMPAIR / ODD ===")
		elif answer=="m" or answer=="M":
			answer = "MANQUE"
			print("\n")
			mprint("=== MANQUE / LOW BET ===")
		elif answer=="p" or answer=="P":
			answer = "PASSE"
			print("\n")
			mprint("=== PASSE / HIGH BET ===")
		return answer
		
def validate_str(string):
	"""A function that checks if a string only contains letters"""
	if not string.isalpha():						
		return None
	return string

