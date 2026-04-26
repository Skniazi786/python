def main():
	from func import cp
	while (True):
		num = input(cp("Type a number please I will tell you if its prime number!: ","cy","bk"))
		if len(num)==0:
			print(cp("Please type something, this is empty space!","bk","r"))
			continue
		elif num.isdigit()==False:
			print(cp("Please type a number because words don't have prime number (>.<)","r","w"))
			continue
		else:
			n=int(num)
			isprime=True
			if (n==1): 
				print(cp("Sorry 1 is not a prime number!","bk","y"))
				break
			elif (n==2): 
				print(cp("2 is a prime number no need to check it.","w","p"))
				break
			else:
				for i in range(2,n):
					if (n%i==0):
						isprime=False
						break
			if (isprime==True):
				print(cp(f"[{n}] is a prime number Congats!.","y","g"))
			else:
				print(cp(f"[{n}] is not a prime number!.","w","cy"))
			break
main()
