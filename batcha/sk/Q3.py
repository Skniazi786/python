from func import cp
	# Importing cp function from my func.py file which only gives me good colouring for terminal.
def Add(a,b):
	return a+b
def Sub(a,b):
	return a-b
def Multi(a,b):
	return a*b
def Div(a,b):
	return a/b
def main():
	funcs = ("add","sub","multi","div","+","-","x","*","/")
	# Storing all could be answers from user regarding these calculations.
	firstry=True
	# If they are trying for first time or again.
	while (True):
		""" Using while loop so if a player makes a mistake he is asked again, 
		everytime he makes a mistake continue restart the program to ask him again."""
		if(firstry==False): print(cp(f"TRY AGAIN MAYBE??!!!!","cy","y"))
		# Error message
		num1 = input(cp("Type first number for calculation ","b","w"))
		print(cp(f"Calculations are these {funcs}","cy","g"))
		cal = input(cp("Type the calculation you want to perform here","c","bk"))
		# Getting inputs from User three times so the program tells if input is valid for calculations.
		num2 = input(cp("Type second number for calculation: ","c","b"))
		if (len(num1)==0 or len(num2)==0 or len(cal)==0):
			print(cp("Please type something, there is empty space here!","bk","r"))
			# Making sure the user doesn't type enter in any input!
			firstry=False
			# Restarting the loop so user know that he is being asked again from the start.
			continue
			# Restart the loop
		elif (num1.isdigit()==False or num2.isdigit()==False or cal.isdigit()==True):
			# Making sure that all the values are correct.
			print(cp("Something is wrong here!","w","r"))
			firstry=False
			# Restarting the loop with error message
			continue
		else:
			cal=cal.lower()
			# Making sure that calculation input is same with my functions
			num1=int(num1)
			num2=int(num2)
			# Converting input which is always a string into Integer for calculations
			if cal not in funcs:
				# If user type something random he is asked again.
				print(cp(f"Please only write calculations you are given!, Add ,Sub ,Multi and Div","bk","y"))
				firstry=False
				# Restarting the loop with error message.
				continue
			else:
				match cal:
					# Using switch clause which is match in python.
					case "add" | "+":
						print(cp(f"Your Answer is [{Add(num1,num2)}] to addition of [{num1}],[{num2}].","y","g"))
					case "sub" | "-":
						print(cp(f"Your Answer is [{Sub(num1,num2)}] if you Subtract [{num2}] from [{num1}].","y","g"))
					case "multi" | "*" |"x":
						print(cp(f"Your Answer is [{Multi(num1,num2)}] to Multiplication of [{num1}],[{num2}].","y","g"))
					case "div" | "/":
						if num2==0:
							# Dividing anything with zero results in error or infinity making sure that doesn't happen.'
							print(cp(f"Sorry You can not divide something by zero.","cy","r"))
							firstry=True
							# Restarting the loop
							continue
						elif num1==num2 : print(cp(f"Your Answer is always 1 if you Divide [{num1}] by [{num2}].","y","g"))
						# No need to calculate same number divided by itself.
						else:
							div = Div(num1,num2)
							print(cp(f"Your Answer is [{int(div) if div == int(div) else round(div,2)}] if you Divide [{num1}] by [{num2}].","y","g"))
			break
main()
