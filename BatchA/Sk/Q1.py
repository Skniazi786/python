def main():
	from func import cp
	# Importing cp function from my func.py file which only gives me good colouring for terminal.
	while (True):
		""" Using while loop so if a player makes a mistake he is asked again, 
		everytime he makes a mistake continue restart the program to ask him again."""
		num = input(cp("Type a number please I will tell you if its prime number!: ","cy","bk"))
		# Getting input from User so the program tells if input is a prime number..
		if len(num)==0:
			print(cp("Please type something, this is empty space!","bk","r"))
			# Making sure the user doesn't type enter before writing anything!
			continue
			# Restart the loop
		elif num.isdigit()==False:
			print(cp("Please type a number because words don't have prime number (>.<)","r","w"))
			# Making sure the user doesn't put letters while user was asked to type number.'
			continue
			# Restart the loop
		else:
			n=int(num)
			# Any input you get from user using input method always a string need to be converted.
			isprime=True
			if (n==1): 
				print(cp("Sorry 1 is not a prime number!","bk","y"))
				# No point in going through 1 as it's a known not a Prime.
				break
				# Breaking the loop
			elif (n==2): 
				print(cp("2 is a prime number no need to check it.","w","p"))
				# No point in going through 2 as well as it is a known Prime.
				break
				# Breaking the loop
			else:
				for i in range(2,n):
					# Starting from 2 as 1 will always return 0 for remainder.
					if (n%i==0):
						isprime=False
						break
						# if a number has a remainder no need to go further breaking the loop
			if (isprime==True):
				print(cp(f"[{n}] is a prime number Congats!.","y","g"))
			else:
				print(cp(f"[{n}] is not a prime number!.","w","cy"))
			break
			# No need to break in upper condition it will automatically break here.
main()
