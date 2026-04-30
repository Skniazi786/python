from func import cp
	# Importing cp function from my func.py file which only gives me good colouring for terminal.
list_by_user=[]
def r_max(mylist):
	c=0
	for i in mylist:
		i=int(i)
		if c<i:
			c=i
	else:
		return c
def main():
	while(True):
		list_size = input(cp("Please type the size of list you want to check for max value :","b","w"))
		if (list_size.strip()==""):
			print(cp("This is empty space! Try again","bk","y"))
			continue
		elif (list_size.isdigit()==False):
			print(cp("Please type a number for list size.","bk","y"))
			continue
		elif (int(list_size) > 10):
			print(cp("Please type a small size for list you can't make very big list","cy","r"))
			continue
		elif (int(list_size)<=1):
			print(cp(f"Your list can't be compared because it doesn't make sense to get max from [{list_size}]","cy","r"))
			continue
		else:
			c=0
			d=int(list_size)
			while(c<d):
				num=input(cp(f"Type a number for list only [{d-c}] Entries left :","b","w"))
				if (num.strip()==""):
					print(cp("Please don't type empty string for this list try again","bk","y"))
					continue
				elif (num.isdigit()==False):
					print(cp("Please type numbers only no words or characters.","cy","r"))
					continue
				else:
					list_by_user.append(num)
					c=c+1
					print(cp(f"Your list uptil now is [{list_by_user}]","y","g"))
			else:
				print(cp(f"Your list was {list_by_user} and the max value is ({r_max(list_by_user)}).","w","b"))
				break
main()
