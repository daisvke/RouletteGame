#!/usr/bin/python3.6

from time import perf_counter
import sys
from random import randrange
from time import sleep
from math import ceil
import json

from package.table import *
from package.board import *
from package.printer import *
from package.croupier import *
from package import end
from package import color
from package.list_manip import *
from package.answer import *
from package.results import *
from package.player import *
from package import new_account

#This is
#RINO MINIMAL CASINO 

# Startup variables declaration
t_start = perf_counter() # Start counting time in seconds
width = os.get_terminal_size().columns # For center display of input
nb_clr = [] # List that will contain colors of each number
nb_clr = color.define_nb_clr() # Now it does
money = 150 # Money possessed by Player at every moment
billionaire = False # To congratulate a new billionaire just once
millionaire = False # To congratulate a new millionnaire just once
almost_millionaire = False # To say that Player is almost millionnaire
play = 1 # The game continues as long as it is true
## p_gain = 0 # Money gained by the Player since the beginning
## r_gain = 0 # Money gained by the casino since the beginning
ex_r_number = 0 # The last number given by the roulette
showed = [] # List of showed roulette numbers
slp = 0.5 # seconds of sleep
player = {} # Dict in which we load data from file 
full_name = ""
last_name = ""
first_name = None
honorific = "Dear Guest"
gender = None
lang = "en" # Language is English by default

# Welcome screen with monochrome roulette table
print("\n\n\n\n")
mprint(" minicasino\n")
mprint(" —  welcome — ")
print("\n\n\n")
sleep(1.5)
color = False # If false, the table is monochrome
table(color)



#######################
### Account Manager ###
#######################

try: # Loop true while not stopped by keyboard
	ln = None
	while not ln: # Player accounts manager
		print("\n")
		if lang == "fr":
			print1by1("Veuillez entrer votre nom de famille,\n")
			print1by1("ou g pour continuer en tant qu'invité.\n\n")
			print1by1("[ English (e) ].\n")
		if lang == "en":
			print1by1("Please type in your last name,\n")
			print1by1("or g to continue as Guest.\n\n")
			print1by1("[ French (f) ].\n")
		print("\n")
		ln = input()
		if ln=="f" or ln=="F": # If chooses French
			lang = "fr"
			ln = None
			continue
		elif ln=="e" or ln=="E": # If chooses English
			lang = "en"
			ln = None
			continue
		# If chooses Guest option, get out from loop with default options
		elif ln=="g" or ln=="G":
			break
		ln = validate_str(ln) # Check if answer only contains letters
		if ln:
			ln = ln.lower()
			ln = ln.capitalize()
		elif not ln:
			if lang == "fr":
				mprint(" Ceci n'est pas un nom.\n") 
			if lang == "en":
				mprint("This is not a name.\n") 
			continue

		if os.path.exists('data.json'): # If the file exists
			f = open('data.json', 'r')
			player = json.load(f)
			f.close()
		print("\n\n")
		i = 1
		keylst = []
		profile_id = [] # List that saves First/Last Names and i values
		for key, value in player.items():
			keylst = key.split(".") 
			if keylst[0] == ln:
				print1by1("({})\n\n".format(i))
				print1by1("First Name: {}\n".format(keylst[1]))
				print1by1("Last Name: {}\n".format(keylst[0]))
				print1by1("Cash: {}\n"\
					.format(space_nb(value["money"])))
				print("\n")
				profile_id.insert(i, keylst) 
				i += 1

		# Generate new account
		if i == 1: # If i stays at 1 = no data
			(ln, full_name, last_name, first_name, 
				player, gender, honorific, 
				money) = new_account.registration(player, lang, ln)
			if ln == None:
				continue
		else:
			answer = 0
			attempt = 0
			while not answer:
				attempt += 1
				sleep(slp)
				if lang == "fr":
					mprint(" Veuillez choisir un compte,\n")
					sleep(slp)
					mprint(" ou entrer n'importe quelle touche pour " \
						"saisir un autre nom.\n")
				elif lang == "en":
					mprint(" Please select your account,\n")
					sleep(slp)
					mprint(" or enter any key to type in another last name.\n")
				answer = input()
				try:
					answer = int(answer)
				except:
					ln = None
					break
				else:
					answer -= 1
					# Get informations on registered Player 
					first_name = profile_id[answer][1]
					last_name = profile_id[answer][0]
					full_name = ".".join(profile_id[answer])
					lang = player[full_name]["lang"]
					money = player[full_name]["money"]
					gender = player[full_name]["gender"]
					honorific = set_honorific(lang, gender)
					break


	#####################
	### Start Betting ###
	#####################

	start_money = money # Money at the beginning
	while play == 1:
		answer = None
		attempt = 0
		more_board = True # Display roulette board if true
		p_bets = [] # List of numbers and bets chosen by the Player
		ex_money = money # Define money before betting this turn

		while not answer or more_board: 
			more_board = False
			more = True # If true Player can stay in loop and keep choosing
			# Display current status and roulette table
			color = True # If True, the red numbers have red background
			table(color)
			sleep(1)
			rest(money) # Display money
			sleep(1)
			# Ask the Player what to bet on
			if lang == "fr":
				mprint("CROUPIER.— Faites vos jeux !")
			elif lang == "en":
				mprint("CROUPIER.— Place your bets !")
			print("\n\n")
			while more:
				attempt += 1 # How many times the loop has been done
				if len(p_bets) > 0:
					if lang == "fr":
						print1by1("* Pour annuler une mise, entrez c *")
					elif lang == "en":
						print1by1("* To cancel a bet, press c *")
					print("\n")
				if lang == "fr":
					print1by1(">>> Plein (0 — 36)\n>>> Rouge, Noir " \
						"(r/b)\n>>> Pair, Impair (e/o)\n>>> " \
						"Manque[1-18], Passe[19-36] (m/p)\n\n* Passer ce " \
						"tour (n)*\n", delay=0.005) 
				elif lang == "en":
					print1by1(">>> Straight Up (0 — 36)\n>>> Red, Black " \
						"(r/b)\n" \
						">>> Even, Odd (e/o)\n>>> Low Bet[1-18], " \
						"High Bet[19-36] (m/p)\n\n* Pass this turn (n)*\n", 
						delay=0.005) 
				answer = input()
				# First, see if the answer is a srting
				if answer=="n" or answer=="N": # For passing turn
					bet = 0
					answer = True
					break
				if answer=="c" or answer=="C": # For bet cancelling
					money = del_bet(lang, honorific, p_bets, money)
					answer = True
					break	
				if find_bet_option(answer):
					answer = edit_bet_option(answer)
				else: # If no color is defined, maybe it is an int
					try: # Try conversion to int
						answer = int(answer)
					except:
						if lang == "fr":
							attempt_level(
								t_start, money, full_name, player, 
								attempt, lang, honorific,
								" CROUPIER.— {}, je n'ai pas saisi...\n"\
									.format(honorific)) 
						elif lang == "en":
							attempt_level(
								t_start, money, full_name, player, 
								attempt, lang, honorific,
								" CROUPIER.— {}, I didn't get that...\n"\
									.format(honorific)) 
						answer = None
						continue
					if answer<0 or answer>36:
						if lang == "fr":
							attempt_level(
								t_start, money, full_name, player, 
								attempt, lang, honorific,
								" CROUPIER.— Non, {}, pas là !\n" \
								"Uniquement sur les cases numérotées !\n"\
									.format(honorific))
						elif lang == "en":
							attempt_level(
								t_start, money, full_name, player, 
								attempt, lang, honorific,
								" CROUPIER.— No, {}, not there !\n" \
								"Only on the numbered squares !\n"\
									.format(honorific))
						answer = None
						continue
					else:
						if answer == 0: # If zero, print green bg
							print("\n")
							mprint("         Number :   == \u001b[42m {} " \
								"\u001b[0m ==".format(answer))
						elif nb_clr[answer] == "rouge": # If zero, print green
							print("\n")
							mprint("         Number :   == \u001b[41m {} " \
								"\u001b[0m ==".format(answer))
						else:
							print("\n")
							mprint("Number :   == {} ==".format(answer))
				print("\n")
				
				# If nbr|clr is set, ask for the amount of bet
				bet = -1
				attempt = 0
				while  bet<0 or bet>money:
					attempt += 1
					rest(money)
					if lang == "fr":
						print1by1(">>> ENTREZ VOTRE MISE (0 => ALL):\n")
					elif lang == "en":
						print1by1(">>> TYPE YOUR BET (0 => ALL):\n")
					bet = input()
					# Conversion of typed number
					try:
						bet = int(bet)
					except:
						if lang == "fr":
							attempt_level(t_start, money, full_name, player, 
								attempt, lang, honorific,
								" CROUPIER.— {}, je n'ai pas saisi...\n"\
									.format(honorific))
						elif lang == "en":
							attempt_level(t_start, money, full_name, player, 
								attempt, lang, honorific,
								" CROUPIER.— {}, I didn't get that...\n"\
									.format(honorific))
						bet = -1
						continue
					if bet < 0:
						if lang == "fr":
							attempt_level(t_start, money, full_name, player,
								attempt, lang, honorific,
								" CROUPIER.— {}, c'est une blague...?\n"\
									.format(honorific))
						elif lang == "en":
							attempt_level(t_start, money, full_name, player,
								attempt, lang, honorific,
								" CROUPIER.— {}, is this a joke...?\n"\
									.format(honorific))
						continue
					if bet > money:
						if lang == "fr":
							attempt_level(t_start, money, full_name, player, 
								attempt, lang, honorific,
								" CROUPIER.— Ah non {}, je regrette, " 
								"vous n'en avez pas les moyens !\n"\
									.format(honorific))
						elif lang == "en":
							attempt_level(t_start, money, full_name, player, 
								attempt, lang, honorific,
								" CROUPIER.— Oh no {}, I'm sorry, " 
								"you don't have enough !\n"\
									.format(honorific))
						continue
					# If no money is left, or if the bet is huge
					if bet==0 or bet==money:
						bet = money
					audacity(lang, honorific, bet, money)
					# Assign number + bet to the list
					# First, let's check if bet already made for elt 
					if find_idem(p_bets, answer, bet):
						edit_idem(p_bets, answer, bet) 
					else : # If not, insert values as new elt in list
						p_bets.insert(0, [answer, bet])
					bet_reg(p_bets) # Display all bets
					money -= bet # And remove amount of bet from money
					break
				rest(money)
				if money <= 0: # If no money, no more bets
					more = False
					answer = 1 # Avoid re-loop
				print("\n")

				sleep(.5)
				answer = None
				attempt = 0
				# Ask if more bets are to be done
				while not answer: 					
					attempt += 1
					if money == 0: # If no money, Player can't bet anymore
						if lang == "fr":
							mprint(" CROUPIER.— Je vous remercie, {}. " \
								"Ce sera tout (y/c) ?\n".format(honorific))
							mprint("* Pour annuler une mise, entrez c*\n")
						elif lang == "en":
							mprint(" CROUPIER.— Thank you, {}. " \
								"Would that be all (y/c) ?\n".format(honorific))
							mprint("* To cancel a bet, press c*\n")
						sleep(.5)
						print("\n")
					elif len(p_bets) == 0: # If no bet, no bet cancelling
						if lang == "fr":
							print1by1(" CROUPIER.— Je vous remercie, {}. " \
								"Ce sera tout (y/n) ?\n".format(honorific))
						elif lang == "en":
							print1by1(" CROUPIER.— Thank you, {}. " \
								"Would that be all (y/n) ?\n".format(honorific))
						print("\n")
					elif money>0 and len(p_bets)>0:
						if lang == "fr":
							print1by1(" CROUPIER.— Je vous remercie, {}. " \
								"Ce sera tout (y/n/c) ?\n* Pour annuler une " \
								"mise, entrez c*\n".format(honorific))
						elif lang == "en":
							print1by1(" CROUPIER.— Thank you, {}. " \
								"Would that be all (y/n/c) ?\n* To cancel a " \
								"bet, press c*\n".format(honorific))
						print("\n")
					answer = input()
					if answer=="c" or answer=="C" : # For bet cancelling
						money = del_bet(lang, honorific, p_bets, money)
						answer = None
						continue	
					elif answer=="y" or answer=="Y": # If chooses to leave
						sleep(.7)
						if lang == "fr":
							mprint(" CROUPIER.— Très bien {} {}, la partie " \
								"peut commencer...\n"\
								.format(edit_honor(lang, honorific), last_name))
						elif lang == "en":
							mprint(" CROUPIER.— Very well {} {}, the game " \
								"can begin...\n"\
								.format(edit_honor(lang, honorific), last_name))

						sleep(.7)
						total_bet = total_column(p_bets, 1) # Sum of bet(s)
						if lang == "fr":
							mprint(" Le total de vos mises est de: {} " \
								"$ !\n".format(space_nb(total_bet)))
						elif lang == "en":
							mprint(" The total amount of your bets is: {} " \
								"$ !\n".format(space_nb(total_bet)))
						sleep(.7)

						if total_bet>(ex_money // 1.5) and total_bet>1000:  
							if lang == "fr":
								mprint(" J'admire votre hardiesse, {} !\n"\
								.format(honorific))
							elif lang == "en":
								mprint(" I admire your audacity, {} !\n"\
								.format(honorific))
							sleep(.7)
						if lang == "fr":
							mprint("Je vous souhaite bonne chance !")	
						elif lang == "en":
							mprint("I wish you good luck !")	
						more = False # End of loop
					elif (answer=="n" or answer=="N") and money>0:
						pass
					else:
						if lang == "fr":
							attempt_level(t_start, money, full_name, player, 
								attempt, lang, honorific,
								" CROUPIER.— {}, je n'ai pas saisi...\n")
						elif lang == "en":
							attempt_level(t_start, money, full_name, player, 
								attempt, lang, honorific,
								" CROUPIER.— {}, I didn't get that...\n")
						answer = None
						continue
				if (answer=="n" or answer=="N" or answer=="c" or answer=="C") \
						and money > 0:
					more_board = True # Display the roulette board again for new bet
					break
		


		################
		### Roulette ###
		################

		# Now we prepare the roulette 
		r_number = randrange(37) # Random number is delivered
		showed.append(r_number) # Add the number to showed numbers' list
		### r_number = 0 # For testing purpose
		r_color = nb_clr[r_number].upper() # Color of number from roulette
		# Check if low bet or high bet
		r_lowhigh = None # If zero, no value
		if r_number>0 and r_number<= 18:
			r_lowhigh = "MANQUE"
		if r_number > 18:
			r_lowhigh = "PASSE"
		# Check if odd or even 
		r_parity = None
		if r_number!=0 and r_number%2 == 0: # Check the parity of the number
			r_parity = "PAIR"
		elif r_number%2 != 0:
			r_parity = "IMPAIR"
		print("\n")

		# Now the game begins !
		spin(r_number, ex_r_number, p_bets) # The roulette spins
		ex_r_number = r_number

		# Announce result according to number/color
		if r_number == 0: # We don't want parity+color if zero
			mprint("         CROUPIER <<< \u001b[42m 0 \u001b[40m ZERO !")
			showed.append(r_number) # Add the number to showed numbers' list
		elif r_color == "ROUGE":
			if lang == "fr":
				mprint("         CROUPIER <<< {} \u001b[41m ROUGE \u001b[40m {} "\
				"!".format(r_number, r_parity))
			elif lang == "en":
				mprint("         CROUPIER <<< {} \u001b[41m RED \u001b[40m {} "\
				"!".format(r_number, r_parity))
		else:
			mprint( \
				"CROUPIER <<< {} {} {} !".format(r_number, r_color, r_parity))
		print("\n\n\n\n")

		# After results are shown :
		# Now we print the Croupier's words according to the situation
		money = results(lang, last_name, honorific, p_bets, money, \
				r_number, r_color, r_parity, r_lowhigh)

		if not billionaire and money>=1000000000 and start_money<1000000000:
			if lang == "fr":
				mprint("           " \
					"\u001b[43m Vous êtes milliardaire !!! \u001b[0m\n")
			elif lang == "en":
				mprint("           " \
					"\u001b[43m You are a billionaire !!! \u001b[0m\n")
			billionaire = True
			millionaire = True
			almost_millionaire = True # We don't need this
		elif not millionaire and money>=1000000 and start_money<1000000:
			if lang == "fr":
				mprint("           " \
					"\u001b[43m Vous êtes millionnaire !!! \u001b[0m\n")
			elif lang == "en":
				mprint("           " \
					"\u001b[43m You are a millionaire !!! \u001b[0m\n")
			millionaire = True
			almost_millionaire = True # We don't need this
		elif not almost_millionaire and money>=800000 and start_money<800000:
			if lang == "fr":
				mprint("           " \
					"\033[93mVous être très proche d'être millionnaire" \
					"\033[0m !\n")
			elif lang == "en":
				mprint("           " \
					"\033[93mYou are very close to being a millionaire" \
					"\033[0m !\n")
			almost_millionaire = True # Avoid saying it twice

		# End of spinning and consequences	
		sleep(1.5)
		rest(money) # Display how much money is left
		if money > 0:
			if lang == "fr":
				mprint(" Il vous reste {0} $.\n".format(space_nb(money)))
			elif lang == "en":
				mprint(" You have {0} $ left.\n".format(space_nb(money)))
			print("\n")
		elif money == 0:
			if lang == "fr":
				mprint("Vous êtes à court d'argent {} ! " \
					"Revenez plus tard !".format(honorific))
			elif lang == "en":
				mprint("You are out of money {} ! " \
					"Come back later !".format(honorific))
			print("\n\n\n")
			end.bye(t_start, lang, money, full_name, player) # Last words + logo
			sys.exit(1)
		"""mprint("Vous voilà endetté {} ! "\
		"Je vous conseille d'arrêter maintenant !\n")
			sys.exit(1)"""
		
		p_gain = money - ex_money # Determine how much Player gained in the end 
		r_gain = p_gain * -1 # Casino gains the opposite value 
		
		# Ask if the Player wants to stay|leave
		play = end.stay_leave(t_start, lang, honorific, full_name, player, \
			p_gain, start_money, money)

except KeyboardInterrupt: # End without error report if stopped by keyboard
	print("\n\n\n")
	end.bye(t_start, lang, money, full_name, player)

