"""A module that generates new account for a new player"""

from time import sleep

from package.printer import *
from package.player import *
from package.list_manip import *
from package.answer import *

def registration(player, lang, ln, slp=0.5): 
	full_name = None
	last_name = None
	first_name = None
	honorific = "Sir"
	gender = "male"
	money = 0

	sleep(slp)
	if lang == "fr":
		mprint(" Il n'y a aucun compte à ce nom.\n")
	elif lang == "en":
		mprint(" There is no account with this name.\n")
	new = None
	while not new:
		sleep(slp)
		if lang == "fr":
			mprint(" Souhaitez-vous créer un nouveau compte " \
			"avec '{}' en tant que nom de famille ? (y/n)\n"\
			.format(ln))
		elif lang == "en":
			mprint(" Would you like to create a new account " \
				"with '{}' as your last name ? (y/n)\n"\
				.format(ln))
		sleep(slp)
		print("\n")
		if lang == "fr":
			mprint(" Si vous désirez vous enregistrer avec un " \
				"autre nom,\n")
			mprint("veuillez saisir n'importe quelle touche.\n")
		elif lang == "en":
			mprint(" If you wish to register with another name, " \
				"please enter any key.\n")
		new = input()
		if new=="y" or new=="Y":
			print("\n")
			mprint(" —   Last Name: {}   —\n".format(ln))
			# Ask first name
			fn = None
			while not fn:
				print("\n")
				sleep(slp)
				if lang == "fr":
					print1by1("Veuillez saisir votre prénom:\n\n")
					sleep(slp)
					print1by1("* Saisissez c pour retourner en " \
						"arrière*\n")
				elif lang == "en":
					print1by1("Please enter your first name:\n\n")
					sleep(slp)
					print1by1("* Enter c to go back *\n")
				fn = input()
				if fn=="c" or fn=="C":
					new = True
					ln = None
					break
				fn = validate_str(fn)
				if not fn:
					if lang == "fr":
						mprint(" Ceci n'est pas un nom.\n") 
					elif lang == "en":
						mprint(" This is not a name.\n") 
			fn = fn.lower()
			fn = fn.capitalize()
			print("\n")
			mprint(" —   First Name: {}   —\n".format(fn))
			# Ask gender
			gd = None
			while not gd:
				print("\n")
				sleep(slp)
				if lang == "fr":
					print1by1("Veuillez indiquez votre sexe:\n\n")
					sleep(slp)
					print1by1("- Homme (m)\n- Femme (f)\n\n")
					sleep(slp)
					print1by1("* Saisissez c pour retourner en " \
						"arrière*\n")
				elif lang == "en":
					print1by1("Please specify your gender:\n\n")
					sleep(slp)
					print1by1("- Male (m)\n- Female (f)\n\n")
					sleep(slp)
					print1by1("* Enter c to go back *\n")
				gd = input()
				if gd=="c" or gd=="C":
					new = True
					ln = None
					break
				elif gd=="m" or gd=="M":
					gd = "male"
				elif gd=="f" or gd=="F":
					gd = "female"
				else:
					gd = None
					if lang == "fr":
						mprint(" Vous n'avez que deux choix.\n")
					elif lang == "en":
						mprint(" You only have two choices.\n")
			mprint(" —   Gender: {}   —\n".format(gd))
			# Ask amount of money to transfer		
			mo = None
			while not mo:
				print("\n")
				sleep(slp)
				if lang == "fr":
					print1by1("Montant des crédits à transférer " \
						"sur votre compte Rino ($)\n")
				elif lang == "en":
					print1by1("Amount of credit to transfer " \
						"to your Rino account ($)\n")
				mo = input()
				try:
					mo = int(mo)
				except:
					if lang == "fr":
						mprint(" Seuls les caractères numériques " \
							"sont autorisés.\n") 
					elif lang == "en":
						mprint(" Only numerical characters " \
							"are allowed.\n") 
					mo = None
				else:
					print("\n")
					sleep(slp)
					if lang == "fr":
						mprint(" Vous êtes sur le point de " \
							"transférer {} $ vers votre compte " \
							"Rino.\n".format(\
							space_nb(mo)))
						sleep(slp)
						mprint(" En êtes-vous certain ? (y/n)\n")
						sleep(slp)
						print1by1("* Saisissez c pour retourner en " \
							"arrière*\n")
					elif lang == "en":
						mprint(" You are about to transfer {} $ " \
							"to your Rino account.\n".format(\
							space_nb(mo)))
						sleep(slp)
						mprint(" Are you sure ? (y/n)\n")
						sleep(slp)
						print1by1("* Enter c to go back *\n")
					answer = None
					while not answer:
						answer = input()
						if answer=="c" or answer=="C":
							new = True
							ln = None
							break
						elif answer=="y" or answer=="Y":
							mprint(" —   Cash: {} $   —\n"\
								.format(space_nb(mo)))
							sleep(slp)
							if lang == "fr":
								mprint(" Je vous remercie !\n")
								sleep(slp)
								mprint(" Votre compte est maintenant " \
									"prêt à être utilisé.\n")
							elif lang == "en":
								mprint(" Thank you !\n")
								sleep(slp)
								mprint(" Now your account is now " \
									"ready to be used.\n")
							sleep(1)
							# Save new profile
							full_name = "{}.{}".format(ln, fn)
							last_name = ln
							first_name = fn
							player[full_name] = {}
							gender = player[full_name]["gender"] = gd
							# Save current language
							player[full_name]["lang"] = lang
							# Create empty record keys 
							player[full_name]["rec_start_money"] = 1
							player[full_name]["rec_money"] = 1
							# Create visit key
							player[full_name]["visits"] = 0
							# Create elapsed time key
							player[full_name]["time"] = 0
							# Set honorific
							honorific = set_honorific(lang, gender)
							# Define money
							player[full_name]["money"] = money = mo
						elif answer=="n" or answer=="N":
							mo = None
							continue
						else:
							answer = None
							if lang == "fr":
								mprint(" Vous n'avez que deux choix.\n")
							elif lang == "en":
								mprint(" You only have two choices.\n")
		elif new=="n" or new=="N":
			player = [] # We empty player data => no saving into file
			sleep(slp)
			if lang == "fr":
				mprint(" Initialisation du jeu en tant qu'invité...\n")
			elif lang == "en":
				mprint(" Beginning game as Guest...\n")
				sleep(1)
		else:
			new = True
			ln = None

		return (ln, full_name, last_name, 
			first_name, player, gender, honorific, money)
