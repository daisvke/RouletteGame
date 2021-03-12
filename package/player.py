"""A module that controls information about the Players."""

import json
from time import perf_counter

def save(t_start, money, full_name, player):
	"""A function that saves modified data of Player."""
	# Save changes in the copy of the file before dumping
	if player and full_name: # If player dict has been loaded from data file

		# How much is gained by the Player  
		# Gain equals to start money - money 
		# If gain is negative, it is a loss	 
		p_gain = money - player[full_name]["money"]		
		
		# How much is gained by the Casino
		# Gain equals to the opposite of the Player's gain value 
		r_gain = p_gain * -1
		
		# Find record ratio of the record saved in file 
		saved_record_ratio = (player[full_name]["rec_money"] 
				/ player[full_name]["rec_start_money"])
		# Find ratio of this game
		new_record_ratio = (money 
				/ player[full_name]["money"])

		# If new ratio is superior to old ratio, we update the record
		if new_record_ratio > saved_record_ratio:
			player[full_name]["rec_money"] = money
			player[full_name]["rec_start_money"] = player[full_name]["money"]

		# Add elapsed time to saved elapsed time
		t_stop = perf_counter()
		player[full_name]["time"] += t_stop - t_start
		## To print in HH:MM:SS : print(datetime.timedelta(seconds=exectime))

		# Update Player and Casino money
		player[full_name]["money"] = money
		player["Casino.Rino"]["money"] += r_gain

		# Add one visit to the visits key value
		player[full_name]["visits"] += 1

		# Save these data
		with open('data.json', 'w') as f:
			json.dump(player, f, sort_keys=True, indent=4)
	
def set_honorific(lang, gender):
	"""A function that sets the honorific according to Player's
	selected language and gender
	"""
	honorific = None
	# French
	if lang=="fr" and gender==None:
		honorific = "Monsieur/Madame"	
	elif lang=="fr" and gender=="male":		
		honorific = "Monsieur"
	elif lang=="fr" and gender=="female":
		honorific = "Madame"

	# English
	if lang=="en" and gender==None:
		honorific = "Sir/Madam"	
	if lang=="en" and gender=="male":		
		honorific = "Sir"
	elif lang=="en" and gender=="female":
		honorific = "Madam"

	return honorific

def edit_honor(lang, honorific):
	"""A function that modifies honorifics according to the context"""
	# French
	if lang=="fr" and honorific=="Monsieur":
		return "M."
	elif lang=="fr" and honorific=="Madame":
		return "Mme."

	# English
	if lang=="en" and honorific=="Sir":
		return "Mr."
	elif lang=="en" and honorific=="Madam":
		return "Mrs."

