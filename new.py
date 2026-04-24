def gtxt(x):
	return "\033[1;92m"+x+"\033[0m"
def btxt(x):
	return "\033[1;96m"+x+"\033[0m"
def rtxt(x):
	return "\033[1;91m"+x+"\033[0m"
def ptxt(x):
	return "\033[1;95m"+x+"\033[0m"
def main():
	word = input(btxt("Please type a word and I will write in reverse without using built in fuctions such as reverse: "))
	if len(word)==0:
		print(rtxt("Please type a word bigger then empty space!"))
		main()
	elif word.isdigit()==True:
		print(rtxt("Please don't type a number type a word!")) 
		main()
	else:
		neww=word
		y=[]
		for w in neww:
			y.append(neww[-1])
			neww=neww[:-1]
		print(gtxt(f"Your real word is  {word} and its reverse is {''.join(y)}"))
main()
