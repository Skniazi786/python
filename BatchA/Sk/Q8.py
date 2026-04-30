from func import cp
	# Importing cp function from my func.py file which only gives me good colouring for terminal.
def find_fibo(a):
	d=[]
	b,c=0,1
	for _ in range(a):
		d.append(b)
		b,c=c,b+c
	else:
		return d
def main():
	while True:
		inp = input(cp("Please type how many first Fibonnaci you want. :","b","w"))
		if (inp.strip()==""):
			print(cp("This is empty space! Try again","bk","y"))
			continue
		elif inp.isdigit() == False:
			print(cp("Please type a number & nothing else!.","bk","y"))
			continue
		elif (int(inp)<0):
			print(cp(f"Makes no sense to find Fibonnaci number till [{inp}].","cy","r"))
			continue
		elif (int(inp)>500):
			print(cp(f"[{inp}] is very high pleae give me small number..","cy","r"))
			continue
		else:
			print(cp(f"Your first ({inp}) Fibonacci numbers are {find_fibo(int(inp))}.","y","g"))
			break
main()
