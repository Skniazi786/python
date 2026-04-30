from func import cp
	# Importing cp function from my func.py file which only gives me good colouring for terminal.
def rem_dups(a):
	b=[]
	for i in a:
		if (i not in b):
			b.append(i)
	else:
		return b 
def main():
	while True:
		list_by_user=[]
		inp = input(cp("Please enter the size of List you want to make :","b","w",inpu=True))
		print(cp(flu=True),end="")
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
			print(cp(f"Can't find duplicates for a list with [{inp}] values try again.","cy","r"))
			continue
		else:
			c=0
			d=int(inp)
			while(c<d):
				num=input(cp(f"Type a number for list only [{d-c}] Entries left :","cy","p",inpu=True))
				print(cp(flu=True),end="")
				if (num.strip()==""):
					print(cp("Please don't type empty string for this list try again","bk","y"))
					continue
				elif(inp.isdigit()==False):
					print(cp("Please type numbers only no words or characters.","cy","r"))
					continue
				else:
					list_by_user.append(num)
					c=c+1
					print(cp(f"Your list uptil now is {list_by_user}","p","w"))
			else:
				print(cp(f"Your list was {list_by_user} and without duplicate is {rem_dups(list_by_user)}.","w","b"))
				break
main()
