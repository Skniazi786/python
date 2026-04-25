def main():
	from func import cp
	while (True):
		num = input(cp("Type a number please I will tell you if its prime number!","b","w"))
		if len(num)==0:
			print(cp("Please type something, this is empty space!","r","y"))
			continue
		elif num.isdigit()==False:
			print(cp("Please type a number because words don't have prime number (>.<)","r","w"))
			continue
		else:
			n=int(num)
			for i in range(1,n):
				for e in range(1,i):
					if i%e==0:
						print(i)
			break
main()
