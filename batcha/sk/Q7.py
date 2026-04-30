from func import cp
	# Importing cp function from my func.py file which only gives me good colouring for terminal.
def cinp(a):
	d = []
	for i in range(len(a)-1,-1,-1):
		d.append(a[i])
	else:
		return d
def main():
	list_by_user=[]
	while True:
		inp = input(cp("Please enter the size of List you want to make :","b","w"))
		if (inp.strip()==""):
			print(cp("This is empty space! Try again","bk","y"))
			continue
		elif inp.isdigit() == False:
			print(cp("Please type a number for list size.","bk","y"))
			continue
		elif (int(inp) > 10):
			print(cp("Please type a small size for list you can't make very big list","cy","r"))
			continue
		elif (int(inp)<=1):
			print(cp(f"Your list can't be reversed because it doesn't make sense to reverse [{inp}].","cy","r"))
			continue
		else:
			c=0
			d=int(inp)
			while(c<d):
				num=input(cp(f"Type a number or word for list only [{d-c}] Entries left :","b","w"))
				if (num.strip()==""):
					print(cp("Please don't type empty string for this list try again","bk","y"))
					continue
				else:
					list_by_user.append(num)
					c=c+1
					print(cp(f"Your list uptil now is {list_by_user}","y","g"))
			else:
				print(cp(f"Your list was {list_by_user} and its reverse is {cinp(list_by_user)}.","w","b"))
				break
main()
