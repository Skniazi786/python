from func import cp
	# Importing cp function from my func.py file which only gives me good colouring for terminal.
def cinp(a):
	c = tuple(a)
	d = []
	for i in range(len(c)-1,-1,-1):
		d.append(c[i])
	else:
		return "".join(d)
def main():
	while True:
		""" Using while loop so if a player makes a mistake he is asked again, 
		everytime he makes a mistake continue restart the program to ask him again."""
		word1 = input(cp("Please give me a number or word and check whether its a palindrome!","b","w"))
		if (word1 == ""):
			# Making sure the user doesn't type enter by mistake!
			print(cp("Empty space is a palindrome no need to check","bk","y"))
			continue
		else:
			word2 = cinp(word1)
			# Making a spare variable so I don't need to use function again.
			if (word1 != word2):
				# If they are not same in reverse so this word is not a palindrome
				print(cp(f"Sorry [{word1}] is not a palindrome! I mean check yourself : [{word2}]","cy","r"))
				continue
			else:
				# Only one posibility remains that this is indeed a palindrome!
				print(cp(f"Yes [{word1}] is a palindrome","y","g"))
				break
main()
