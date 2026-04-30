from func import cp
	# Importing cp function from my func.py file which only gives me good colouring for terminal.
def rnum(a):
	b=0
	for _ in a:
		b=b+1
	else:
		return b
def main():
	while (True):
		""" Using while loop so if a player makes a mistake he is asked again, 
		everytime he makes a mistake continue restart the program to ask him again."""
		inp = input(cp("Please give me numbers I will tell you how many digits it has.","b","w"))
		# Getting inputs from User
		if (inp == ""):
			# Making sure the user doesn't type enter by mistake!
			print(cp("Please type something this is empty space!","bk","r"))
			continue
			# Restart the loop
		elif (inp.isdigit()==False):
			print(cp("Please type numbers these are not number","w","r"))
			# Making sure that user didn't write letters and not numbers
			continue
			# Restart the loop
		else:
			print(cp(f"Your numbers are [{inp}] and it has [{rnum(inp)}] digits.","y","g"))
			break
			# Breaking the loop ending the program
main()
