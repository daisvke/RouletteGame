"""A module that prints out the lines of the Croupier."""

from time import sleep
import sys
from package.printer import *
from package import end
from package.player import *

def attempt_level(t_start, money, full_name, player, 
	attempt, lang, honorific, words):
	"""A Function that displays Croupier's warnings according to attempt level
	and situation.
	"""
	if attempt>0 and attempt<=3:
		print("\n")
		mprint(words)
		be_serious(t_start, money, full_name, player, attempt, lang, honorific)
	if attempt > 3:
		be_serious(t_start, money, full_name, player, attempt, lang, honorific)

def be_serious(t_start, money, full_name, player, attempt, lang, honorific, 
	slp=0.5):
	"""A function that prints warning from the Croupier
	when the Player is fooling around with the keyboard.
	"""
	# Begin warnings 
	if attempt == 1:
		sleep(slp)
		if lang == "fr":
			mprint(" Encore une fois, je vous prie !\n")
		elif lang == "en":
			mprint(" Once again, please !\n")
	elif attempt == 2:
		sleep(slp)	
		if lang == "fr":
			mprint(" Allez, encore une fois, je vous prie !\n")
		elif lang =="en":
			mprint(" Come on, once again, please !\n")
	elif attempt == 3:
		sleep(slp)
		if lang == "fr":
			mprint(" Soyez sérieux !\n")
		elif lang == "en":
			mprint(" Be serious !\n")
	elif attempt==4:
		sleep(slp)
		if lang == "fr":
			mprint(" CROUPIER.— ...{}, vous le faites exprès ?\n"\
				.format(honorific)) 
			sleep(slp)
			mprint(" Allez-y, je vous en prie !\n")
		elif lang == "en":
			mprint(" CROUPIER.— ...{}, are you doing this on purpose ?\n"\
				.format(honorific))
			sleep(slp)
			mprint("Go ahead, please !\n")
	elif attempt == 5:
		sleep(slp)
		if lang == "fr":
			mprint(" CROUPIER.— {}, si cela continue, vous allez devoir " \
				"vous en aller.\n".format(honorific))
		elif lang == "en":
			mprint(" CROUPIER.— {}, if it goes on like this, I will have to " \
				"ask you to leave.\n".format(honorific))
	elif attempt == 6:
		sleep(slp)
		if lang == "fr":
			mprint(" CROUPIER.— {}, dernier avertissement...\n"\
				.format(honorific))
		elif lang == "en":
			mprint(" CROUPIER.— {}, last warning...\n".format(honorific))
	elif attempt == 7:
		sleep(slp)
		mprint(" ===========================================================" \
			"=============\n")
		if lang == "fr":
			mprint(" CROUPIER.— {}, vous avez gagné !\n".format(honorific)) 
			sleep(slp)
			mprint(" Non pas la partie qui se joue ici sur la table, mais " \
				"une autre :\n") 
			sleep(slp)
			mprint(" celle de L'INDÉCENCE !\n") 
			sleep(slp)
			mprint(" Les agents de sécurité qui viennent d'arriver " \
				"vont vous rediriger vers la sortie.\n")
			sleep(slp)
			mprint(" Et ne revenez plus ici, si c'est pour nous faire " \
				"perdre notre temps !\n")
			sleep(slp)
			mprint(" Adieu, {} !\n".format(honorific))
		elif lang == "en":
			mprint(" CROUPIER.— {}, you have won !\n".format(honorific)) 
			sleep(slp)
			mprint(" Not the game that is being played here on this table," \
				"but an other one :\n") 
			sleep(slp)
			mprint(" it is called INDECENCY !\n") 
			sleep(slp)
			mprint(" The security who have just arrived is going to take you " \
				"out.\n")
			sleep(slp)
			mprint(" and do not come back here if you are going to waste" \
				"our time !\n")
			sleep(slp)
			mprint(" Farewell, {} !\n".format(honorific))
			
		mprint(" ===========================================================" \
			"=============\n\n")
		print("\n\n\n")
		end.bye(t_start, lang, money, full_name, player)
		sys.exit(1)
	print("\n")

def audacity(lang, honorific, bet, money, slp=0.5):
	"""A function that expresses the audacity of Player according to bets."""
	if bet==money:
		if bet>50 and bet< 500:
			if lang == "fr":
				mprint(" CROUPIER.— Vous en avez du courage, {} !\n"\
					.format(honorific))
			elif lang == "en":
				mprint(" CROUPIER.— You have such courage, {} !\n"\
					.format(honorific))
			sleep(slp)
		elif bet>=500 and bet<5000:
			if lang == "fr":
				mprint(" CROUPIER.— Quelle audace, {}...!\n"
					.format(honorific))
			elif lang == "en":
				mprint(" CROUPIER.— How daring, {}...!\n"
					.format(honorific))
			sleep(slp)
		elif bet>=5000 and bet<10000:
			if lang == "fr":
				mprint(" CROUPIER.— Votre mise est incroyable, {}...!\n"\
					.format(honorific))
			elif lang == "en":
				mprint(" CROUPIER.— Your bet is amazing, {}...!\n"\
					.format(honorific))
			sleep(slp)
		elif bet>=10000:
			if lang == "fr":
				mprint(" CROUPIER.— Vous en êtes certain, {}..?\n"\
					.format(honorific))
			elif lang == "en":
				mprint(" CROUPIER.— Are you sure of this, {}..?\n"\
					.format(honorific))
			sleep(slp)
		if lang == "fr":
			mprint(" Vous avez misé la totalité de vos avoirs !\n")
		elif lang == "en":
			mprint(" You have bet all your cash !\n")
	elif bet!=money and bet>=5000 and bet<10000:
		if lang == "fr":
			mprint(" CROUPIER.— Voilà une belle mise, {}...!\n"\
				.format(honorific))
		elif lang == "en":
			mprint(" CROUPIER.— What a nice bet, {}...!\n"\
				.format(honorific))
		sleep(slp)
	elif bet!=money and bet>=10000:
		if lang == "fr":
			mprint(" CROUPIER.— Vous en êtes certain, {}...?\n"\
				.format(honorific))
		elif lang == "en":
			mprint(" CROUPIER.— You are sure of this, {}...?\n"\
				.format(honorific))
		sleep(slp)
	if lang == "fr":
		mprint(" Votre mise est de {} $ !\n".format(space_nb(bet)))
	elif lang == "en":
		mprint(" Your bet is {} $ !\n".format(space_nb(bet)))
	sleep(slp)

