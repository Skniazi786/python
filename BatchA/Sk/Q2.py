def main():
	from func import cp
	# Importing cp function from my func.py file which only gives me good colouring for terminal.
	while (True):
		""" Using while loop so if a player makes a mistake he is asked again, 
		everytime he makes a mistake continue restart the program to ask him again."""
		num = input(cp("Type a number so I can tell you how many prime numbers are can it have!: ","cy","bk"))
		# Getting input from User so the program tells about prime numbers.
		if len(num)==0:
			print(cp("Please type something, this is empty space!","bk","r"))
			# Making sure the user doesn't type enter before writing anything!
			continue
			# Restart the loop
		elif num.isdigit()==False:
			print(cp("Please type a number because words don't have prime numbers (>.<)","r","w"))
			# Making sure the user doesn't put anything but numbers.
			continue
			# Restart the loop
		else:
			n=int(num)
			# Any input you get from user using input method always a string need to be converted.
			el=[]
			# Making an empty list so I can store all the prime numbers.
			if (n==1): 
				print(cp("Sorry 1 is not a prime number!","bk","y"))
				# No point in going through 1 as it's a known not a Prime.
				break
				# Breaking the loop
			elif (n==2): 
				print(cp("2 is a single prime number!","w","p"))
				# No point in going through 2 as well as it is a known Prime.
				break
				# Breaking the loop
			elif (n>541):
				# Making sure the user doesn't type a huge number which would crash his pc.'
				print(cp(f"Something is wrong with you man!, give me a smaller number!","w","p"))
				continue
			else:
				for i in range(2,n+1):
					# Outer Loop  starting from 2 and n+1 because range doesn't go till n it stopes before n.'
					isprime=True
					# Making sure that isprime is always true
					for e in range(2,i):
						# Inner loop Starting from 2 as 1 will always return 0 for remainder.
						if (i%e==0):
							# Checking to see remainder!
							isprime=False
							# If there is a remainder its false.
							break
							# no need to continue further breakng out of inner loop.
					if isprime==True:
						# if its true then it means it can store the prime number
						el.append(i)
						# Append means to store the value at the end of list.
			if  (len(el)>1):
				# Making sure that our list has atleast 2 values.
				print(cp(f"There are [{len(el)}] prime numbers till [{n}]","y","g"))
				# Writing how many prime numbers are there in this number.
				print(cp(f"{el}","y","g"))
				# Writing all the prime numbers from start.
			break
			# No need to break in upper condition it will automatically break here.
main()
