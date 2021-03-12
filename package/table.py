"""module containing the Roulette Table."""

from time import sleep
import sys
from package.printer import *

#	mprint("            /\u001b[42m    0   \u001b[40m\ ") # To make zero green
def table(color):
	"""A function displaying the Roulette Table.
	
	If color is True, red numbers appear with a red backgroud
	"""
	# First, print the monochrome version
	if not color:
		mprint("\n")
		mprint("  ________  ") 
		mprint(" /||||0|||\ ") 
		mprint("|----------|")
		mprint("|1  | 2 | 3|")
		mprint("|----------|")
		mprint("|4  | 5 | 6|")
		mprint("|----------|")
		mprint("|7  | 8 | 9|")
		mprint("|----------|")
		mprint("|10 |11 |12|")
		mprint("|----------|")
		mprint("|13 |14 |15|")
		mprint("|----------|")
		mprint("|16 |17 |18|")
		mprint("|----------|")
		mprint("|19 |20 |21|")
		mprint("|----------|")
		mprint("|22 |23 |24|")
		mprint("|----------|")
		mprint("|25 |26 |27|")
		mprint("|----------|")
		mprint("|28 |29 |30|")
		mprint("|----------|")
		mprint("|31 |32 |33|")
		mprint("|----------|")
		mprint("|34 |35 |36|")
		mprint(" ¯¯¯¯¯¯¯¯¯¯ ")
		sleep(1)
		print("\n\n\n\n")
	
	elif color:
		# Then print it with red squares 
		mprint("\n")
		mprint("  ________  ") 
		mprint(" /||||0|||\ ") 
		mprint("|----------|")
		mprint("                     " \
			"|\u001b[41m1  \u001b[40m| 2 |\u001b[41m 3\u001b[40m|")
		mprint("|----------|")
		mprint("           " \
			"|4  |\u001b[41m 5 \u001b[40m| 6|")
		mprint("|----------|")
		mprint("                     " \
			"|\u001b[41m7  \u001b[40m| 8 |\u001b[41m 9\u001b[40m|")
		mprint("|----------|")
		mprint("           |10 |11 |\u001b[41m12\u001b[40m|")
		mprint("|----------|")
		mprint("           " \
			"|13 |\u001b[41m14 \u001b[40m|15|")
		mprint("|----------|")
		mprint("                     " \
			"|\u001b[41m16 \u001b[40m|17 |\u001b[41m18\u001b[40m|")
		mprint("|----------|")
		mprint("                     " \
			"|\u001b[41m19 \u001b[40m|20 |\u001b[41m21\u001b[40m|")
		mprint("|----------|")
		mprint("           " \
			"|22 |\u001b[41m23 \u001b[40m|24|")
		mprint("|----------|")
		mprint("                     " \
			"|\u001b[41m25 \u001b[40m|26 |\u001b[41m27\u001b[40m|")
		mprint("|----------|")
		mprint("           |28 |29 |\u001b[41m30\u001b[40m|")
		mprint("|----------|")
		mprint("           " \
			"|31 |\u001b[41m32 \u001b[40m|33|")
		mprint("|----------|")
		mprint("                     " \
			"|\u001b[41m34 \u001b[40m|35 |\u001b[41m36\u001b[40m|")
		mprint(" ¯¯¯¯¯¯¯¯¯¯ ")

