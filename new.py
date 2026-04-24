def gtxt(x):
	return "\033[1;92m"+x+"\033[0m"
def btxt(x):
	return "\033[1;96m"+x+"\033[0m"
def rtxt(x):
	return "\033[1;91m"+x+"\033[0m"
def ptxt(x):
	return "\033[1;95m"+x+"\033[0m"
def main():
	num = input(btxt("Please type a number and I will write a factorial for it: "))
	if len(num)==0:
		print(rtxt("Please type a word bigger then empty space!"))
		main()
	elif num.isdigit()==False:
		print(rtxt("Please don't type a word type a Number!")) 
		main()
	else:
		nnum = int(num)
		y=1
		while (nnum>0):
			y=y*nnum
			nnum-=1
		print(gtxt(f"Your number is  [{num}] and its factorial is [{y}]"))
main()
